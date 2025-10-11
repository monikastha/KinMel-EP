from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
class User(AbstractUser):
    ROLES=(
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('vendor', 'Vendor'),
        ('buyer', 'Buyer'),
        ('deliveryman','Deliveryman'),
    )
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address= models.TextField(blank=True, null=True)
    name= models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length = 255)
    role = models.CharField(max_length= 50, choices=ROLES)
    def __str__(self):
        return self.username
    
class Admin(models.Model):
    username = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
admin.site.register(Admin)