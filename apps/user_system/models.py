from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.db import models


class Model_users (AbstractUser,PermissionsMixin):
    email = models.EmailField(unique=True, max_length=250)
    username = models.CharField(unique=True, max_length=50)
    img = models.ImageField(upload_to='img_users', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    creation = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username", "is_superuser"]
    
    def __str__(self):
        return f"User: {self.username}"
    
    def save(self,*args, **kwargs):
        self.username = self.username.capitalize()
        super().save(*args, **kwargs)