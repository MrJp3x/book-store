from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None
    username = None

    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

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
