from rest_framework import generics

from users.api.serializers import SchoolsSerializer
from users.models import Schools

__all__ = ('ListAvailableSchoolsView',)


class ListAvailableSchoolsView(generics.ListAPIView):
    serializer_class = SchoolsSerializer
    queryset = Schools.objects.all()
