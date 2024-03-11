import xlsxwriter
from django.conf import settings
from xlsxwriter import Workbook
from xlsxwriter.worksheet import Worksheet

from users.models import User


def generate_file(list_users: list, file_path: str) -> str:
    """
    Generate file with students information

    :param list_users: List of users
    :param file_path: Path to file
    :return: Path to file
    """
    workbook = _get_workbook(file_path)
    worksheet = _get_worksheet(workbook)

    _add_topic_to_worksheet(worksheet)
    add_users_to_worksheet(worksheet, list_users)

    workbook.close()
    return file_path


def _add_topic_to_worksheet(worksheet: Worksheet) -> None:
    """
    Add topic to worksheet

    :param worksheet: Worksheet
    :return: None
    """
    for index, entry in enumerate(settings.LIST_TOPICS):
        worksheet.write(0, index, entry)


def add_users_to_worksheet(worksheet: Worksheet, list_users: list[User]) -> None:
    """
    Add users to worksheet

    :param worksheet:
    :param list_users:
    :return:
    """
    for index, entry in enumerate(list_users):
        for key, value in entry.to_xlsx_format().items():
            worksheet.write(index + 1, list(entry.to_xlsx_format().keys()).index(key), str(value))


def _get_worksheet(workbook) -> Worksheet:
    """
    Creates a new worksheet and adds it to the given workbook.

    Parameters:
    workbook (Workbook): The workbook object to which the new worksheet will be added.

    Returns:
    Worksheet: The newly created worksheet.
    """
    return workbook.add_worksheet('Sheet')


def _get_workbook(file_path: str) -> Workbook:
    """
    Create a new workbook using the given file path.

    :param file_path: The file path where the workbook will be saved.
    :type file_path: str

    :return: The created workbook.
    :rtype: Workbook
    """
    return xlsxwriter.Workbook(file_path)
