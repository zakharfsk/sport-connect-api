from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import AverageValuesStandards
from sport_connect_api.models import BaseModel
from users.querysets import SchoolQuerySet, SchoolClassesQuerySet


class User(AbstractUser, BaseModel):
    user_school = models.ForeignKey('Schools', on_delete=models.CASCADE, blank=True, null=True)
    user_classroom = models.ForeignKey('SchoolsClassrooms', on_delete=models.CASCADE, blank=True, null=True)
    user_gender = models.CharField(choices=(
        ('Дівчина', 'Дівчина'),
        ('Юнак', 'Юнак')),
        max_length=256, blank=False, null=False)
    user_age = models.IntegerField(choices=((10, 10), (11, 11)), blank=False, null=True)

    def to_xlsx_format(self):
        return {
            'id': self.id,
            'Ім\'я': self.first_name,
            'Прізвище': self.last_name,
            'Стать': self.user_gender,
            'Вік': self.user_age,
            'Школа': self.user_school.school_name,
            'Клас': f'{self.user_classroom.representation()}'
        }

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Користувачі'
        verbose_name = 'Користувач'


class Schools(BaseModel):
    school_name = models.CharField(max_length=256, blank=False, null=False)
    school_city = models.CharField(max_length=256, blank=False, null=False)

    objects = SchoolQuerySet.as_manager()

    def __str__(self):
        return self.school_name

    class Meta:
        db_table = 'schools'
        verbose_name_plural = 'Школи'
        verbose_name = 'Школа'


class SchoolsClassrooms(BaseModel):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    class_number = models.IntegerField(blank=False, null=True)
    class_letter = models.CharField(choices=(
        ('А', 'А'),
        ('Б', 'Б'),
        ('В', 'В'),
        ('Г', 'Г'),
        ('Д', 'Д'),
        ('Е', 'Е'),
        ('Ж', 'Ж'),
        ('З', 'З'),
        ('И', 'И'),
        ('К', 'К'),
        ('Л', 'Л'),
        ('М', 'М'),
        ('Н', 'Н'),
        ('О', 'О'),
        ('П', 'П'),
        ('Р', 'Р'),
        ('С', 'С'),
        ('Т', 'Т'),
        ('У', 'У'),
        ('Ф', 'Ф'),
        ('Х', 'Х'),
        ('Ц', 'Ц'),
        ('Ч', 'Ч'),
        ('Ш', 'Ш'),
        ('Щ', 'Щ'),
        ('Ь', 'Ь'),
        ('Ю', 'Ю'),
        ('Я', 'Я')
    ), max_length=1, blank=False, null=True)

    objects = SchoolClassesQuerySet.as_manager()

    def representation(self):
        return f'{self.class_number}-{self.class_letter}'

    def __str__(self):
        return f'{self.class_number}-{self.class_letter}'

    class Meta:
        db_table = 'schools_classrooms'
        verbose_name_plural = 'Класи'
        verbose_name = 'Клас'


"""
170 - значення яке прийшло з таблиці
137.4 - константа, яка є в бд
4.5 - константа(сігма), яка є в бд


for res in file_result:
    for user_standards, value in res['standards'].items():
        average = AverageValuesStandards.objects.get(name_standard=user_standards,
                                                    children_age=res['Вік'], children_gender=res['Стать'])
        result = 50 + 10 * ((value - average.average_value) / average.sigma)
    

result = 50 + 10 * ((170 - 134.7) / 4.5)
[{
    'id': 1,
    'Зріст, см': result,
    'Біг 30 м/с': result,
    ...
},
...
]
"""

