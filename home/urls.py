from django.contrib import admin
from django.urls import path, include
from home.views import index_view, home_view  # Make sure the import is correct
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('home/', home_view, name='home'),
    path('cybersecurity/', views.cybersecurity_view, name='cybersecurity')
]