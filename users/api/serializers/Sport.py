from rest_framework import serializers

from core.models import Sport

__all__ = ("SportSerializer",)


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"
