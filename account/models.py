from django.contrib.auth.models import AbstractUser
from django.db import models


# todo: 3 tables for each user that inherit User : )
class User(AbstractUser):
    USER_ROLE = (
        ('normal', 'User'),
        ('publisher', 'Book Publisher'),
    )

    role = models.CharField(max_length=20, choices=USER_ROLE)
    profile_picture = models.ImageField(upload_to='static/profile_pictures/', blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)

    # company_name = models.CharField(max_length=255, blank=True, null=True)
    # company_address = models.TextField(blank=True, null=True)
    # tax_number = models.CharField(max_length=20, blank=True, null=True)

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
