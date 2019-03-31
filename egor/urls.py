from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    path('<int:id>', views.info, name="info"),
]