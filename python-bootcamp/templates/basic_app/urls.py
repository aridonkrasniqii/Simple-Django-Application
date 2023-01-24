from django.urls import path
from basic_app import views

# you need to set up the name of the file to let django now about it
# when you work with relative urls
# and set the view name if you call it at html file
# path('', views.method , name='name of the template')
app_name = 'basic_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('base/', views.base, name='base'),
    path('relative', views.relative, name='relative'),
]
