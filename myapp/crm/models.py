from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    # Add custom fields here if needed
    pass

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Add other fields here

class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=50, default="Unknown Company")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50, default="CEO")
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return(f'{self.company} {self.position} {self.first_name} {self.last_name} {self.email} {self.phone}')
