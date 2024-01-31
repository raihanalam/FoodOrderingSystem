from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Additional fields for customers
    # favorite_restaurant = models.ForeignKey('Restaurant', on_delete=models.SET_NULL, blank=True, null=True)

    # Additional fields for vendors
    restaurant_name = models.CharField(max_length=100, blank=True, null=True)
    restaurant_description = models.TextField(blank=True, null=True)
    restaurant_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username