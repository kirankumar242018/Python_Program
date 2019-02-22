from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):  # class custom user takes the models fields credentials
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):  # returns the fields information
        return self.email
