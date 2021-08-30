from django.contrib import admin
from django.urls import path, include

from .views import home

app_name = 'webpage'

urlpatterns = [

  path('', home, name="home"),
   
]


