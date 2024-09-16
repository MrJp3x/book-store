from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager, AbstractUser
from utils.models import TimeStamp


def avatar_upload_path(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = f"{instance.user.email}.{extension}"
    return f'media/avatar/{new_filename}'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('باید فیلد ایمیل وارد شود')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('سوپریوزر باید is_staff=True داشته باشد.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('سوپریوزر باید is_superuser=True داشته باشد.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    first_name = None
    last_name = None
    username = None

    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.is_admin = False

    class Meta:
        permissions = [
            ('view_user', 'Can view user'),
        ]
        default_permissions = ()
        swappable = 'AUTH_USER_MODEL'


class Profile(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    avatar = models.ImageField(upload_to=avatar_upload_path , null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
