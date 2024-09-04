from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('profiles/', include('profiles.urls')),  # URLs for the profiles app
    path('users/', include('users.urls')),  # URLs for the users app
    path('', user_views.home, name='home'),  # Home page view
    path('about/', user_views.about, name='about'),  # About page view (updated to use user_views)
    path('contact/', user_views.contact, name='contact'),  # Contact page view (updated to use user_views)
    path('accounts/', include('allauth.urls')),  # allauth URLs for authentication
    path('accounts/', include('django.contrib.auth.urls')),  # Django's built-in auth URLs
    path('trashcollection/', include('trashcollection.urls')),  # Include the app URLs


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development
