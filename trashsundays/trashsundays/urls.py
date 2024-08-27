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
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('', include('django.contrib.auth.urls')),  # Django's built-in auth URLs
]