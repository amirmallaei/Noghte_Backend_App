from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core import validators
import uuid

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number is required")
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user = self.model(phone_number = phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
            extra_fields.setdefault("is_staff", True)
            extra_fields.setdefault("is_superuser", True)
    
            if extra_fields.get("is_staff") is not True:
                raise ValueError("Superuser must have is_staff=True.")
            if extra_fields.get("is_superuser") is not True:
                raise ValueError("Superuser must have is_superuser=True.")
            return self.create_user(phone_number, password=None, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    first_name = models.CharField(verbose_name=_("First Name"),max_length=50, blank=True)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=50, blank=True)
    phone_number = models.BigIntegerField(verbose_name=_("Phone No."), unique=True, 
                    validators=[validators.RegexValidator(regex=r"989\d{9}")],
                    error_messages=("A user with the phone number already exists")
                    )
    email = models.EmailField(verbose_name=_("Email"), unique=True, blank=True, null=True)

    is_staff = models.BooleanField(verbose_name=_("is Staff"), default=False, 
                                   help_text="Whether User can Login into Admin panel")
    
    is_active = models.BooleanField(verbose_name=_("is Active"),default=True, 
                                    help_text="Whether User can login or not")
    
    date_joined = models.DateTimeField(verbose_name=_("Date Joined"), 
                                       auto_created=True, null=True, blank=True)

    USERNAME_FIELD = "phone_number"

    objects = UserManager()