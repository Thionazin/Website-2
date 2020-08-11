from django.urls import path
from . import views

urlpatterns = [
    path('', views.showcase_index, name="index"),
]