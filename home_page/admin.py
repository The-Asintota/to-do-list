from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser


class UserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_staff', 'is_active', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

admin.site.register(CustomUser, UserAdmin)