from typing import Dict, List

from rest_framework import serializers

from users.models import Schools, SchoolsClassrooms

__all__ = ('SchoolsSerializer',)


class SchoolsSerializer(serializers.ModelSerializer):
    school_classrooms = serializers.SerializerMethodField()

    def get_school_classrooms(self, obj) -> List[Dict[str, str]]:
        return SchoolsClassrooms.objects.get_list_classrooms_by_school(obj.id)

    class Meta:
        model = Schools
        fields = '__all__'
