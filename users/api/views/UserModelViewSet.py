from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.api.serializers import ShowUserSerializer, UpdateUserSerializer

__all__ = ('UserModelViewSet',)


class UserModelViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    @swagger_auto_schema(responses={200: openapi.Response('User info', ShowUserSerializer)})
    def me(self, request):
        serializer = ShowUserSerializer(request.user)
        return Response(serializer.data)

    @me.mapping.put
    @swagger_auto_schema(responses={200: openapi.Response('User info', UpdateUserSerializer)})
    def update_me(self, request):
        serializer = UpdateUserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @me.mapping.delete
    def delete_me(self, request):
        user = request.user
        user.delete()
        return Response(status=204)
