from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class WeatherModel(models.Model):
    id_city = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    temperature = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    max_temperature = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    min_temperature = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    api_resource = models.CharField(max_length=70, null=True, blank=True)
    temperature_month_ago = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    temperature_year_ago = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    temperature_yesterday = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
