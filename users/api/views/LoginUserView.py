from django.contrib.auth import authenticate, login
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.api.serializers import LoginUserSerializer
from users.models import User

__all__ = ('LoginUserView',)


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
