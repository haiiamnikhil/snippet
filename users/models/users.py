import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), unique=True, max_length=30)

    class Meta:
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email
