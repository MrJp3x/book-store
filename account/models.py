from django.contrib.auth.models import AbstractUser
from django.db import models


class UserConst(models.TextChoices):
    NORMAL = 'normal', 'User'
    PUBLISHER = 'publisher', 'Book Publisher'


class User(AbstractUser):

    role = models.CharField(max_length=20, choices=UserConst.choices)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.role == 'publisher':  # todo: hard code
            self.is_admin = True
        else:
            self.is_admin = False
        super(User, self).save(*args, **kwargs)

    class Meta:
        permissions = [
            ('view_user', 'Can view user'),
        ]
        default_permissions = ()
        swappable = 'AUTH_USER_MODEL'
        unique_together = [['username']]
