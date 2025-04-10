import requests
from core.models import UserResult
from config.celery import celery_app
from core.services.calculate_result import calculation
from users.models import User


@celery_app.task
def calculate_formula_results(file_path: str):
    exel_data = calculation.get_data_from_excel(file_path)
    standards = calculation.calculate_standards_result(exel_data)
    results = calculation.calculate_sports_aptitude(standards)

    for result in results:
        UserResult.objects.create(
            user_id=result["id"],
            result=result["sport_results"],
            standards=result["standards"],
        )
        user = User.objects.get(id=result["id"])
        requests.post(
            "https://exp.host/--/api/v2/push/send",
            json={
                "to": f"ExponentPushToken[{user.fcm_token}]",
                "title": "Результати готові!",
                "body": "Результати тестування доступні в додатку клацай та дивись!!!",
            },
        )

    return results
