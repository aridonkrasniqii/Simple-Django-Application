from django.urls import path
from TempApp import views



urlpatterns = [
    path('', views.index, name='index'),
]
