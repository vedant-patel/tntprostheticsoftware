from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('testarm', views.testarm, name='testarm'),
    path('index', views.index, name='index'),
    path('middle', views.middle, name='middle'),
    path('ring', views.ring, name='ring'),
    path('pinky', views.pinky, name='pinky'),
]
