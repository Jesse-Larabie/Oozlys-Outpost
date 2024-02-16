from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
   path('', include('home.urls')),  # Assuming your app is named 'home'
    path('cybersecurity/', include('cybersecurity.urls')),  # Assuming another app is named 'cybersecurity'
    
]
