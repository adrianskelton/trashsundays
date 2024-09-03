from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_trash_collection, name='add_trash_collection'),
]