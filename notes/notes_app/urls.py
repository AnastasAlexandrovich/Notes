from django.template.backends import django
from django.urls import path, include

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.sign_in, name='login'),
    path('add-note', views.add_note),
    path('save-note', views.save_note),
    path('all-notes', views.all_notes, name='all_notes'),
    path('logout', views.sign_out, name='logout')
]
