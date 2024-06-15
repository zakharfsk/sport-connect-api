from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, viewsets
from rest_framework.response import Response

from core.api.serializers import UserResultSerializer

__all__ = ('UserResultListAPIView', 'LastUserResultRetrieveAPIView',)

from core.models import UserResult


class UserResultListAPIView(generics.ListAPIView):
    serializer_class = UserResultSerializer
    queryset = UserResult.objects.all().order_by('-date_created')


class LastUserResultRetrieveAPIView(viewsets.ViewSet):
    serializer_class = UserResultSerializer
    queryset = UserResult.objects.all().order_by('-date_created').first()

    @swagger_auto_schema(responses={200: openapi.Response('Last user result', UserResultSerializer)})
    def get(self, request):
        serializer = self.serializer_class(self.queryset)
        return Response(serializer.data)
