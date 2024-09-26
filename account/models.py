from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager, AbstractUser
from utils.models import TimeStamp
from .const import sex_choice, user_type_choice, admin_type_choice


def avatar_upload_path(instance, filename):
    """
      Generates the upload path for avatars based on the user's email.

      Args:
          instance (AbstractBaseProfile): The instance of the profile model.
          filename (str): The original filename of the uploaded file.

      Returns:
          str: The generated upload path for the avatar.
    """
    extension = filename.split('.')[-1]
    new_filename = f"{instance.user.email}.{extension}"
    return f'media/avatar/{new_filename}'


# region user
class CustomUserManager(BaseUserManager):
    """
    Custom user manager for creating regular and superusers.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a regular user with the given email and password.

        Args:
            email (str): The email of the user.
            password (str, optional): The password for the user. Defaults to None.
            **extra_fields: Additional fields to set on the user.

        Returns:
            User: The created user instance.

        Raises:
            ValueError: If the email is not provided.
        """
        if not email:
            raise ValueError('باید فیلد ایمیل وارد شود')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
         Creates and saves a superuser with the given email and password.

         Args:
             email (str): The email of the superuser.
             password (str, optional): The password for the superuser. Defaults to None.
             **extra_fields: Additional fields to set on the superuser.

         Returns:
             User: The created superuser instance.

         Raises:
             ValueError: If 'is_staff' or 'is_superuser' fields are not True.
         """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser is not staff.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('account is not superuser.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Custom user model that uses email as the unique identifier.

    Attributes:
        email (str): The email address of the user.
        phone (str): The phone number of the user.
        user_type (str): The type of the user.
    """
    first_name = None
    last_name = None
    username = None

    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=14, unique=True, null=True, blank=True)
    user_type = models.CharField(choices=user_type_choice, max_length=20, null=True, blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        """
        Returns a string representation of the user.

        Returns:
            str: The email of the user.
        """
        return self.email

    def __init__(self, *args, **kwargs):
        """
        Initializes the User instance and sets the admin status to False.
        """
        super(User, self).__init__(*args, **kwargs)
        self.is_admin = False

    class Meta:
        """
        Meta information for the User model.

        Attributes:
            permissions (list): Custom permissions for the user model.
            default_permissions (tuple): Disables default permissions.
            swappable (str): Allows swapping with a custom user model.
        """
        permissions = [
            ('view_user', 'Can view user'),
        ]
        default_permissions = ()
        swappable = 'AUTH_USER_MODEL'


# endregion


# region profile

class AbstractBaseProfile(TimeStamp):
    """
    Abstract base class for profiles with common fields and methods.

    Attributes:
        user (User): The user associated with the profile.
        avatar (ImageField): The profile picture of the user.
        address (str): The address of the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to=avatar_upload_path, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the profile.

        Returns:
            str: The email or phone number of the user, or 'No Email or Phone'.
        """
        final_field = self.user.email if self.user.email else self.user.phone
        return final_field

    class Meta:
        """
        Returns a string representation of the profile.

        Returns:
            str: The email or phone number of the user, or 'No Email or Phone'.
        """
        abstract = True  # This class will not be created as a table in the database.


class UserProfileAbstract(AbstractBaseProfile):
    """
    User profile abstract class with personal information.

    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        sex (str): The gender of the user.
        birth_date (date): The birthdate of the user.
    """
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    sex = models.CharField(max_length=10, blank=True, null=True, choices=sex_choice)
    birth_date = models.DateField(blank=True, null=True)  # TODO: person calendar (jalali time)

    def __str__(self):
        """
        Returns a string representation of the user profile.

        Returns:
            str: The full name of the user.
        """
        return f'{self.first_name} {self.last_name}'


class PublisherProfileAbstract(AbstractBaseProfile):
    """
    Publisher profile abstract class with company-related fields.

    Attributes:
        publisher_manager (str): The name of the manager of the publisher.
        company_name (str): The name of the company.
        website (URLField): The website of the publisher.
        established_year (int): The year the company was established.
        publisher_logo (ImageField): The logo of the publisher.
    """
    publisher_manager = models.CharField(max_length=22, blank=False, null=False)
    company_name = models.CharField(max_length=32, blank=False, null=False)
    website = models.URLField(blank=False, null=False)
    established_year = models.PositiveSmallIntegerField(blank=False, null=False)
    publisher_logo = models.ImageField(upload_to=avatar_upload_path, null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the publisher profile.

        Returns:
            str: The company name.
        """
        return f'{self.company_name}'


class AdminProfileAbstract(AbstractBaseProfile):
    """
    Admin profile abstract class with administrative information.

    Attributes:
        first_name (str): The first name of the admin.
        last_name (str): The last name of the admin.
        address (str): The address of the admin.
        sex (str): The gender of the admin.
        birth_date (date): The birthdate of the admin.
        admin_type (str): The type of admin.
    """
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.TextField(max_length=150, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True, choices=sex_choice)
    birth_date = models.DateField(blank=True, null=True)  # TODO: person calendar (jalali time)
    admin_type = models.CharField(choices=admin_type_choice, max_length=20, null=True, blank=True)

# endregion
