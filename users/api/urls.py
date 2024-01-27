from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from users.api.views import LoginUserView, RegisterUserView, ListAvailableSchoolsView, UserModelViewSet

app_name = 'users'

router = DefaultRouter()

router.register('users', UserModelViewSet, basename='users')

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('list/schools/', ListAvailableSchoolsView.as_view(), name='list_schools'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]
