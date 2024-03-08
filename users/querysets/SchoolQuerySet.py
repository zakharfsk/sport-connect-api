from django.db import models

__all__ = ('SchoolQuerySet',)


class SchoolQuerySet(models.QuerySet):
    def get_list_schools(self):
        return [(f'{school.id}', f'{school.school_name}') for school in self.all()]
