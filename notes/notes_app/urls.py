from django.template.backends import django
from django.urls import path, include

from . import views

urlpatterns = [
    path('index', views.index),
    path('register', views.register, name='register'),
    path('login', views.signin, name='login'),
    path('add-note', views.add_note),
    path('save-note', views.save_note)
]
