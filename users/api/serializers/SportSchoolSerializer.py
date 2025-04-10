from rest_framework import serializers

from core.models import SportSchool


class SportSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportSchool
        fields = [
            "id",
            "school_name",
            "school_site_url",
            "school_sport_address",
            "school_sport_email",
            "school_sport_phone_numbers",
        ]
