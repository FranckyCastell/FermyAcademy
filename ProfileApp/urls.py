from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('profile', views.profile, name='profile')
]
