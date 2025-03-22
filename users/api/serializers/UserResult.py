from rest_framework import serializers

from core.models import UserResult

__all__ = ('UserResultSerializer',)


class UserResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResult
        exclude = ('user',)
