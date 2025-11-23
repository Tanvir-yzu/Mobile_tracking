from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # ✅ This includes all the above routes
    path('', include('devices.urls')),
    path('', include('tracking.urls')),
]