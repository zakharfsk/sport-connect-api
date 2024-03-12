from rest_framework import serializers

from users.models import User

__all__ = ('LoginUserSerializer',)


class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password')
