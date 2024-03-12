from rest_framework import serializers

from users.models import User

__all__ = ('ShowUserSerializer',)


class ShowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'password',
            'groups',
            'user_permissions',
            'is_staff',
            'is_superuser',
        )
