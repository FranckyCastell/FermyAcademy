from django.urls import path
from ReserveApp import views

urlpatterns = [
    path('reserve', views.reserve, name='reserve')
]
