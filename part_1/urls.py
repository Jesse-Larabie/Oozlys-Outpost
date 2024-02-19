from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='part_1'),
]
