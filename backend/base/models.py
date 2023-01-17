from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class WeatherModel(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    temperature_pos = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    temperature_neg = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    temperature_curr = models.CharField(max_length=5, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    max_temperature = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    min_temperature = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    api_resource = models.CharField(max_length=70, null=True, blank=True)
    temperature_month_ago = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    temperature_year_ago = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    temperature_yesterday = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class ArchivedWeatherModel(models.Model):
    weather_model = models.ForeignKey(WeatherModel, on_delete=models.SET_NULL, null=True)
    temperature_pos_arch = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    temperature_neg_arch = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    temperature_curr_arch = models.CharField(max_length=5, blank=True, null=True)
    description_arch = models.TextField(null=True, blank=True)
    max_temperature_arch = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    min_temperature_arch = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    api_resource_arch = models.CharField(max_length=70, null=True, blank=True)
    temperature_month_ago_arch = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    temperature_year_ago_arch = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    temperature_yesterday_arch = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.temperature_pos_arch)
