from sport_connect_api.celery import app
from core.services.calculate_result.calculation import get_data_from_excel, calculate_standards_result, calculate_sports_aptitude


@app.task
def calculate_formula_results(file_path: str):
    exel_data = get_data_from_excel(file_path)
    standards = calculate_standards_result(exel_data)
    result = calculate_sports_aptitude(standards)
    return result
