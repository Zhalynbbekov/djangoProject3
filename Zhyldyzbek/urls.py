from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello, name='home'),
    path('command/', views.command, name='command')
]
