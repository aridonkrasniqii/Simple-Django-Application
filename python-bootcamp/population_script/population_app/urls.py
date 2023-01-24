from django.urls import path
from population_app import views

urlpatterns = [
    path('', views.index , name='index')
]
