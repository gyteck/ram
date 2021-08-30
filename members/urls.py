from django.urls import path, include
from .views import UserRegisterView


urlpatterns = [
    path('', UserRegisterView.as_view(),name="register"),

]
