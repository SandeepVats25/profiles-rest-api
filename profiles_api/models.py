from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for User Profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile """
        if not email:
            raise ValueError('User Must Have An Email Address')
        email = self.normalize_email(email)
        user = self.mode(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, password):
        """ creates and save a new superuser with given details """
        user =self.create_user(email, name, password)

        user.is_superuser = true
        user.is_staff = true
        user.save(using=self.db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in System """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default =True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retireve Full Name of Users"""
        return self.name

    def get_short_name(self):
        """retireve short name"""
        return self.name

    def __str__(self):
        """Return String Reperestation of our user"""
        return self.email
