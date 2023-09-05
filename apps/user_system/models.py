from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.db import models


class Model_users (AbstractUser,PermissionsMixin):
    email = models.EmailField(unique=True, max_length=250)
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='img_users', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    creation = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name',"username"]
    
    def __str__(self):
        return f"User: {self.username}"
    
    def save(self,*args, **kwargs):
        self.username = self.username
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        super().save(*args, **kwargs)