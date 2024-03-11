from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from users.api import views

app_name = 'users'

router = DefaultRouter()

router.register('users', views.UserModelViewSet, basename='users')

urlpatterns = [
    path('auth/register/', views.RegisterUserView.as_view(), name='register'),
    path('auth/login/', views.LoginUserView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('schools/', views.ListAvailableSchoolsView.as_view(), name='list_schools'),
    path('', include(router.urls))
]
