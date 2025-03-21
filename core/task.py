from core.models import UserResult
from config.celery import celery_app
from core.services.calculate_result import calculation


@celery_app.task
def calculate_formula_results(file_path: str):
    exel_data = calculation.get_data_from_excel(file_path)
    standards = calculation.calculate_standards_result(exel_data)
    results = calculation.calculate_sports_aptitude(standards)

    for result in results:
        UserResult.objects.create(user_id=result['id'], result=result["sport_results"],standards=results["standards"])

    return results
