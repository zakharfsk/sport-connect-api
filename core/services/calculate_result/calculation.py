"""
Функція має повертати список словників в вигляді:

[
  {
    "id": "",
    "first_name": "",
    "last_name": "",
    "gender": ""
    "age": "",
    "school": "",
    "classrom": "",
    "standards": {
      "Назва_екзамену": "результат дитини"
    }
  }
]
"""
from openpyxl import load_workbook
from django.conf import settings
from django.core.files.storage import default_storage
from django.db.models import Q

from core.models import AverageValuesStandards, Sport, WeightingFactors


def get_data_from_excel(file_path: str) -> list:
    wb = load_workbook(file_path)
    ws = wb.active
    data = []

    for j in range(2, ws.max_row + 1):
        d = {}
        for i, key in enumerate(settings.LIST_TOPICS, start=1):
            val = ws.cell(row=j, column=i).value
            if val is not None:
                if i > 7:
                    d.setdefault("standards", dict())
                    d["standards"][key] = val
                else:
                    d[key] = val
        d["standards"]["Вагово-ростовий індекс (індекс маси тіла), маса (гр), зріст (см)"] = d["standards"]['Зріст, см'] / \
            d["standards"]['Маса, гр']
        d["standards"]["Індекс розвитку мускулатури (периметр плеча напруженого/периметр плеча розслабленого)"] = d["standards"]['Периметр плеча напруженого, см'] /\
            d["standards"]['Периметр плеча розслабленого, см']
        data.append(d)
    default_storage.delete(file_path)

    return data


def calculate_standards_result(file_result: list):
    data = []
    for res in file_result:
        d = {"id": res["id"]}
        for user_standards, value in res['standards'].items():
            try:
                average = AverageValuesStandards.objects.get(
                    name_standard=user_standards,
                    children_age=res['Вік'],
                    children_gender=res['Стать']
                )
                result = 50 + 10 * ((value - average.average_value) / average.sigma)
                d[user_standards] = result
            except AverageValuesStandards.DoesNotExist:
                continue
        data.append(d)
    return data


def calculate_sports_aptitude(standards_result: list):
    result_dict = {}
    for sport in Sport.objects.all():
        weight_factors = dict(
            WeightingFactors.objects.filter(sport=sport.pk)
            .values_list("average_value_standard__name_standard", "weighting_factor")
        )

        for st_res in standards_result:
            res = 0
            for key, value in st_res.items():
                if key in weight_factors:
                    res += value * weight_factors[key]
            result_dict[sport.name] = res
    return result_dict
