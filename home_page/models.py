from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.apps import apps
from django.db import models


class CustomUserManager(UserManager):
    
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email address.')
        if not username:
            raise ValueError('User must have a username.')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    
    Email and password are required. Other fields are optional.
    """
    
    email = models.EmailField(
        _('email'),
        unique=True,
        max_length=80,
    )
    username = models.CharField(
        _("username"),
        null=False,
        blank=False,
        unique=True,
        max_length=80,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    
    objects = CustomUserManager()
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        
        verbose_name = _("user")
        verbose_name_plural = _("users")
    
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return self.username

    def get_short_name(self):
        """Return the short name for the user."""
        return self.username or self.email.split('@')[0]



