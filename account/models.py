from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    role = models.CharField(max_length=20, choices=UserConst.choices)
    phone = models.CharField(max_length=11, blank=True, null=True)
    is_phone_verified = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.is_admin = False

    def save(self, *args, **kwargs):
        self.is_admin = self.role == UserConst.PUBLISHER
        super(User, self).save(*args, **kwargs)

    class Meta:
        permissions = [
            ('view_user', 'Can view user'),
        ]
        default_permissions = ()
        swappable = 'AUTH_USER_MODEL'
