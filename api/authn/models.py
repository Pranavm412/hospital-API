from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not name:
            raise ValueError('Name is required')
        email=self.normalize_email(email)
        user=self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, name, password=None):
        email=self.normalize_email(email)
        return self.create_user(email=email, name=name, password=password, is_staff=True, is_superuser=True)

class User(AbstractBaseUser, PermissionsMixin):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254, unique=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    objects=UserManager()

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["name"]

    def __str__(self):
        return self.email