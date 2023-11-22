from django.urls import path

from .views import register, homepage

urlpatterns = [
    path('', homepage),
    path('register', register),
]