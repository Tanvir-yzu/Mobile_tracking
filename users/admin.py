from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register CustomUser with Django's default UserAdmin (works with AbstractUser)
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')