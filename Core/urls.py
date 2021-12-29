from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AboutApp.urls')),
    path('', include('ContactApp.urls')),
    path('', include('CoursesApp.urls')),
    path('', include('HomeApp.urls')),
]
