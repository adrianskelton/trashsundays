from django.urls import path, include
from . import views
from trashcollection import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('trashcollection/', include('trashcollection.urls')),  # Include the URLs for the trashcollection app
] 
