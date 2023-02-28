from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('upload_csv_view/',views.upload_csv_view,name='upload_csv_view'),
    path('train.html',views.train,name='train')
    


]
