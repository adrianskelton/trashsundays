from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.log_trash, name='log_trash'),
]