from django.urls import path
from .views import AddTrashCollectionView  # Import the renamed class-based view
from . import views

urlpatterns = [
    path('map/', views.user_map, name='user_map'),
    path('add/', AddTrashCollectionView.as_view(), name='add_trash_collection'),  # Use .as_view() for class-based views
]


