from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', views.get_routes, name="routes"),
    path('test/', views.get_test_data, name="routes"),
    path('users/profile/', views.get_user_profile, name='user_profile'),
    path('api/users/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair')
]
