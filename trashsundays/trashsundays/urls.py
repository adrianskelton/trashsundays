from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include your user-related URLs
    path('', user_views.home, name='home'),  # Home page view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('', include('django.contrib.auth.urls')),  # Django's built-in auth URLs
]