from django.contrib import admin
from django.urls import include, path
from home.views import index_view, home_view  # Import views from the 'home' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),  # Map the index view to the root URL
    path('home/', home_view, name='home'),  # Map the home view to the /home/ URL
    path('cybersecurity/', include('cybersecurity.urls')),  # Assuming another app is named 'cybersecurity'
    path('part_1/', include('part_1.urls')),
    path('part_2/', include('part_2.urls')),
    path('part_3/', include('part_3.urls')),
    path('part_4/', include('part_4.urls')),
    path('part_5/', include('part_5.urls')),
    path('part_6/', include('part_6.urls')),
    path('part_7/', include('part_7.urls')),
    path('part_8/', include('part_8.urls')),
    path('personal_projects/', include('personal_projects.urls')),
]
