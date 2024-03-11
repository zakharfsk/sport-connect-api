from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('get_file/', views.get_file_for_student_calculation, name='get_file'),
    path('upload_result/', views.upload_results, name='upload_result'),
]
