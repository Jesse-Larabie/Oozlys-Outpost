from django.urls import path
from . import views


urlpatterns = [
    path('', views.cybersecurity_index, name='cybersecurity_index'),
]