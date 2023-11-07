# Python imports
import uuid

# PIP imports
from django.contrib.auth.models import AbstractUser
from django.db import models


LENGTH_MEDIUM = 128


class User(AbstractUser):
    """Custom User model"""

    first_name = models.CharField(blank=True, max_length=LENGTH_MEDIUM, null=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    last_name = models.CharField(blank=True, max_length=LENGTH_MEDIUM, null=True)
    modified = models.DateTimeField(auto_now=True)
