from django.conf.urls import url
from django.urls import path

from admin.weather import views

urlpatterns = {
    url(r'process', views.process)
}