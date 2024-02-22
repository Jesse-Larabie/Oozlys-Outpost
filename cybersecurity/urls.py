from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),  # Include URLs from the 'home' app
    path('cybersecurity/', include('cybersecurity.urls')),  # Include URLs from the 'cybersecurity' app
    # Other paths...
]