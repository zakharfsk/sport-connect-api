from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.api.serializers import RegisterUserSerializer
from users.models import User

__all__ = ('RegisterUserView',)


@extend_schema(tags=['Authorization'])
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
