from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', views.get_routes, name="routes"),
    path('test/', views.get_test_data, name="test_json"),
    path('users/profile/', views.get_user_profile, name='user_profile'),
    path('users/get_users/', views.get_users, name='get_users'),
    path('users/register_user/', views.register_user, name='register_user'),
    path('api/users/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair')
]
