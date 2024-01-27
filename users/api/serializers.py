from rest_framework import serializers

from users.models import User, Schools, SchoolsClassrooms


class RegisterUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    user_school = serializers.PrimaryKeyRelatedField(queryset=Schools.objects.all(), required=True,
                                                     pk_field=serializers.UUIDField())
    user_classroom = serializers.PrimaryKeyRelatedField(queryset=SchoolsClassrooms.objects.all(), required=True,
                                                        pk_field=serializers.UUIDField())
    user_age = serializers.IntegerField(required=True)

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


class ShowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions', 'is_staff', 'is_superuser',)


class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password')


class SchoolsSerializer(serializers.ModelSerializer):
    school_classrooms = serializers.SerializerMethodField()

    def get_school_classrooms(self, obj):
        return SchoolsClassrooms.objects.get_list_classrooms_by_school(obj.id)

    class Meta:
        model = Schools
        fields = '__all__'
