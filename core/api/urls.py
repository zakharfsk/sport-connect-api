from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserResultListAPIView.as_view(), name='user_result_list'),
    path('last/', views.LastUserResultRetrieveAPIView.as_view({'get': 'get'}), name='last_user_result'),
]
