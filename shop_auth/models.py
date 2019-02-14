from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

# Create your models here.

class CustomUser(AbstractUser):
    country = CountryField(blank_label='(select country)')
    address = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.username