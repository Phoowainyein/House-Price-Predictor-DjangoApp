from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    # path('upload_csv_view/',views.upload_csv_view,name='upload_csv_view'),
    path('train.html',views.train,name='train'),
    path('train_model/', views.train_model, name='train_model'),
    path('predict.html',views.predict,name='predict'),
    path('predict_model/', views.predict_model, name='predict_model'),
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
