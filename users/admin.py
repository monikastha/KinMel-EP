from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.0
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id','name','username','email','phone','address','role','password','is_active']
    list_filter = ['is_active', 'role']
    search_fields = ['username', 'email','name']

admin.site.register(User, CustomUserAdmin)
