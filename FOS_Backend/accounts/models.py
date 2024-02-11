from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class UserProfile(AbstractUser):
    class Meta:
        app_label = 'accounts'

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



    # Specify custom related_name for groups and user_permissions fields
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='user_profiles'  # Custom related_name for groups
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='user_profiles'  # Custom related_name for user_permissions
    )

    def __str__(self):
        return self.username