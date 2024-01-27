from sport_connect_api.celery import app
from core.services.calculate_result import calculation


@app.task
def calculate_formula_results(file_path: str):
    exel_data = calculation.get_data_from_excel(file_path)
    standards = calculation.calculate_standards_result(exel_data)
    result = calculation.calculate_sports_aptitude(standards)
    return result
