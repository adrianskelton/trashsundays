from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include your user-related URLs
    path('', user_views.home, name='home'),  # Home page view
    path('about/', auth_views.LoginView.as_view(template_name='about.html'), name='about'),
    path('contact/', auth_views.LoginView.as_view(template_name='contact.html'), name='contact'),
    path('accounts/', include('allauth.urls')),  # allauth URLs
    path('', include('django.contrib.auth.urls')),  # Django's built-in auth URLs
]