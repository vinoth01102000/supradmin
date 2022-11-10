from typing import List

import django.db
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your CustomUserManager here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, first_name, last_name, mobile, password, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)

# Create your User Model here.
class User(AbstractBaseUser,PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default

    email = django.db.models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = django.db.models.CharField(max_length=240)
    last_name = django.db.models.CharField(max_length=255)
    mobile = django.db.models.CharField(max_length=50)
    address = django.db.models.CharField(max_length=250)

    is_staff = django.db.models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_active = django.db.models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = django.db.models.BooleanField(default=False) # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS:str = ['first_name','last_name','mobile']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

#
# from django.core.management.base import BaseCommand, CommandError
# from django.contrib.auth.models import User
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         # The magic line
#         User.objects.create_user(username='rmx',
#                                  email='superuser@super.com',
#                                  password='rmx55',
#                                  is_staff=True,
#                                  is_active=True,
#                                  is_superuser=True
#                                  )


# Create your models here.
