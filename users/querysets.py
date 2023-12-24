from django.db import models


class SchoolQuerySet(models.QuerySet):
    def get_list_schools(self):
        return [(f'{school.id}', f'{school.school_name}') for school in self.all()]


class SchoolClassesQuerySet(models.QuerySet):
    def get_list_classrooms_by_school(self, school_id):
        return [
            {'classroom': f'{school_classroom.class_number}-{school_classroom.class_letter}',
             'classroom_id': school_classroom.id} for school_classroom in self.filter(school=school_id)
        ]

    def get_list_classrooms_classes(self):
        return [
            f'{school_classroom.class_number}-{school_classroom.class_letter}' for school_classroom in self.all()
        ]
