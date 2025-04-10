from rest_framework import generics
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

from core.models import SportSchool
from users.api.serializers import SportSchoolSerializer


@extend_schema(tags=["Sports"])
class ListSportSchoolsView(generics.ListAPIView):
    queryset = SportSchool.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SportSchoolSerializer

    def get_queryset(self):
        sport_id = self.kwargs.get("sport_id")
        return SportSchool.objects.filter(sport_id=sport_id)
