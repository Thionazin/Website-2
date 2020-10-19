from django.urls import path
from . import views

urlpatterns = [
    path('', views.academics, name="academics"),
]
