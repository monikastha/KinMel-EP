from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.0
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'username', 'email', 'role', 'is_active', 'is_staff',
                     'is_superuser','updated_at','password','last_login','first_name',
                    'last_name','date_joined']
    list_filter = ['is_active', 'role']
    search_fields = ['username', 'email'
                     ,'first_name']

admin.site.register(User, CustomUserAdmin)
