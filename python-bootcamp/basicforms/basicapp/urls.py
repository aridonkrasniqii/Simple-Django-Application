from django.urls import path
from basicapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_page/', views.form_name, name='form_name')
]
