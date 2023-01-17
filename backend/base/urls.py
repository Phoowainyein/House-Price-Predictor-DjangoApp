from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.get_routes, name="routes"),
    path('test/', views.get_test_data, name="routes"),
    path('api/users/login', TokenObtainPairView.as_view(), name='token_obtain_pair')
]
