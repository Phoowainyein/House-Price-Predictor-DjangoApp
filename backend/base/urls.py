from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name="routes"),
    path('test/', views.get_test_data, name="routes"),
]
