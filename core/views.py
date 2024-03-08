import os
import uuid

from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.utils.encoding import escape_uri_path

from core.task import calculate_formula_results

from core.services.exel_file_generator.generator import generate_file
from users.models import User


def get_file_for_student_calculation(request: WSGIRequest):
    if request.method == 'POST':

        list_users = User.objects.filter(user_school=request.POST['choose_school'],
                                         user_classroom=request.POST['choose_school_classroom'])

        if not list_users.exists():
            return HttpResponseNotFound('<h1>Users not exist</h1>')

        list_users = list_users.all()

        school = list_users[0].user_school.school_name
        classroom = list_users[0].user_classroom.representation()
        file = generate_file(list_users, settings.BASE_DIR /
                             f'{school} {classroom}.xlsx')

        try:
            response = HttpResponse(open(file, 'rb'),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;'
                                                 'charset=utf-8')
            response['Content-Disposition'] = (f"attachment;"
                                               f"filename*=utf-8''{escape_uri_path(f'{school} {classroom}.xlsx')}")

            return response
        except IOError:
            return HttpResponseNotFound('<h1>File not exist</h1>')
        finally:
            os.remove(file)

    return render(
        request,
        'core/get_file_for_student_calculation.html',
    )


def upload_results(request: WSGIRequest):
    if request.method == 'POST':
        file: InMemoryUploadedFile = request.FILES.get('file_with_results')
        file_path = os.path.join(settings.CALCULATIONS_FILES_FOLDER, f"{uuid.uuid4()}.xlsx")

        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # function for printing data from file

        result = calculate_formula_results.delay(file_path)
        # Path to function for core/services/calculate_result/calculation.py

    return render(request, 'core/upload_file_with_result.html')
