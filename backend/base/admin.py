from django.contrib import admin
from .models import WeatherModel, ArchivedWeatherModel
# Register your models here.

admin.site.register(WeatherModel)
admin.site.register(ArchivedWeatherModel)
