from rest_framework.reverse import reverse_lazy

from core.models import UserResult
from sport_connect_api.celery import app
from core.services.calculate_result import calculation
from sport_connect_api.pusher import trigger_event


@app.task
def calculate_formula_results(file_path: str):
    exel_data = calculation.get_data_from_excel(file_path)
    standards = calculation.calculate_standards_result(exel_data)
    results = calculation.calculate_sports_aptitude(standards)

    for result in results:
        UserResult.objects.create(user_id=result['id'], result=result)
        trigger_event(
            result['id'],
            'results-calculated',
            {
                'message': 'Results calculated successfully',
                'url': str(reverse_lazy('core_api:last_user_result'))
            }
        )

    return results
