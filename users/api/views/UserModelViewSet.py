from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import UserResult
from users.api.serializers import ShowUserSerializer, UpdateUserSerializer

__all__ = ('UserModelViewSet',)

from users.api.serializers.UserResult import UserResultSerializer


@extend_schema(tags=['Users'])
class UserModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    @extend_schema(exclude=True)
    def list(self, request, *args, **kwargs):
        return Response({'detail': 'Method not allowed'}, status=405)

    @extend_schema(exclude=True)
    def create(self, request, *args, **kwargs):
        return Response({'detail': 'Method not allowed'}, status=405)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        return Response({'detail': 'Method not allowed'}, status=405)

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        return Response({'detail': 'Method not allowed'}, status=405)

    @extend_schema(exclude=True)
    def partial_update(self, request, *args, **kwargs):
        return Response({'detail': 'Method not allowed'}, status=405)

    @extend_schema(exclude=True)
    def destroy(self, request, *args, **kwargs):
        return Response({'detail': 'Method not allowed'}, status=405)

    def get_serializer_class(self):
        if self.action == 'me':
            return ShowUserSerializer
        if self.action == 'update_me':
            return UpdateUserSerializer
        return ShowUserSerializer

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = ShowUserSerializer(request.user)
        return Response(serializer.data)

    @me.mapping.put
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

    @extend_schema(responses=UserResultSerializer(many=True))
    @action(detail=False, methods=['get'])
    def results(self, request):
        serializer = UserResultSerializer(UserResult.objects.filter(user=request.user).all(), many=True)
        return Response(serializer.data)

    @extend_schema(responses=UserResultSerializer)
    @action(detail=False, methods=['get'], url_path='results/last')
    def last_result(self, request):
        serializer = UserResultSerializer(
            UserResult.objects.filter(user=request.user).order_by('-date_created').first()
        )
        return Response(serializer.data)
