from django.urls import path
from . import views

urlpatterns = [
    path('', views.showcase_index, name="index"),
    path('<int:pk>/', views.showcase_detail, name="detail"),
]