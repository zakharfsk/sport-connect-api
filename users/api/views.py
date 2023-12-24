from rest_framework import generics

from users.api.serializers import RegisterUserSerializer, SchoolsSerializer
from users.models import User, Schools


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()


class ListAvailableSchoolsView(generics.ListAPIView):
    serializer_class = SchoolsSerializer
    queryset = Schools.objects.all()


class ListAvailableSchoolClassesView(generics.ListAPIView):
    serializer_class = None
    queryset = Schools.objects.all()
