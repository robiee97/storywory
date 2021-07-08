from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self,username,email,fullname,password=None):
        if username is None:
            raise TypeError('User should have username')
        if email is None:
            raise TypeError('User should have email')

        user= self.model(username=username,fullname=fullname,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username,email,fullname,password=None):
        if password is None:
            raise TypeError('User should have password')
        
        user= self.create_user(username,email,fullname,password)
        user.is_superuser= True
        user.is_staff= True
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):

    username=models.CharField(max_length=255,unique=True,db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    fullname = models.CharField(max_length=60, blank=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(default='avatar.png')
    
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects= UserManager()

    def __str__(self):
        return self.username
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {'refresh': str(refresh),'access': str(refresh.access_token)}

    

