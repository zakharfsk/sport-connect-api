from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.models import Sport
from users.api.serializers import SportSerializer

__all__ = ("ListSportView",)


@extend_schema(tags=["Sports"])
class ListSportView(generics.ListAPIView):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()
    permission_classes = (IsAuthenticated,)
