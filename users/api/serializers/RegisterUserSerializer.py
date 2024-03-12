from rest_framework import serializers

from users.models import Schools, SchoolsClassrooms, User

__all__ = ('RegisterUserSerializer',)


class RegisterUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    user_school = serializers.PrimaryKeyRelatedField(queryset=Schools.objects.all(),
                                                     pk_field=serializers.UUIDField(),
                                                     required=True)
    user_classroom = serializers.PrimaryKeyRelatedField(queryset=SchoolsClassrooms.objects.all(),
                                                        pk_field=serializers.UUIDField(),
                                                        required=True)
    user_age = serializers.ChoiceField(choices=((10, 10), (11, 11)), required=True)
    user_gender = serializers.ChoiceField(choices=(('Дівчина', 'Дівчина'), ('Юнак', 'Юнак')), required=True)

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name', 'email',
                  'user_school', 'user_classroom',
                  'user_gender', 'user_age', 'password')
        write_only_fields = ('password',)
