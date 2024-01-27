from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login

from users.api.serializers import LoginUserSerializer, RegisterUserSerializer, SchoolsSerializer, ShowUserSerializer
from users.models import User, Schools


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        user = get_object_or_404(User, email=request.data['email'])

        tokens = RefreshToken.for_user(user)

        return Response({
            'refresh': str(tokens),
            'access': str(tokens.access_token),
        })


class LoginUserView(generics.CreateAPIView):
    serializer_class = LoginUserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer: LoginUserSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, email=serializer.validated_data['email'])
        auth_user = authenticate(request, username=user.username, password=serializer.validated_data['password'])

        if not auth_user:
            return Response({
                'error': 'Invalid credentials'
            }, status=401)

        login(request, auth_user)
        tokens = RefreshToken.for_user(user)

        return Response({
            'refresh': str(tokens),
            'access': str(tokens.access_token),
        })


class UserModelViewSet(viewsets.ViewSet):
    serializer_class = ShowUserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = ShowUserSerializer(request.user)
        return Response(serializer.data)


class ListAvailableSchoolsView(generics.ListAPIView):
    serializer_class = SchoolsSerializer
    queryset = Schools.objects.all()
