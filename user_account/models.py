from django.db import models
from home_page.models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Task(models.Model):
    
    name = models.CharField(
        _('Title'),
        null=False,
        blank=False,
        max_length=80,
    )
    description = models.CharField(
        _('Description'),
        null=False,
        blank=False,
        max_length=300,
    )
    important = models.BooleanField(_('Important'), default=False,)
    date_created = models.DateTimeField(_('date created'), default=timezone.now,)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )


