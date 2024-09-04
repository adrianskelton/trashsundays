from django.urls import path
from .views import TrashCollection  # Import TrashCollection from views.py

urlpatterns = [
    #path('add/', TrashCollection, name='add_trash_collection'),
    path('add/', TrashCollection.as_view(), name='add_trash_collection'),

]