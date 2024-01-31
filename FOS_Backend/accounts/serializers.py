from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'is_customer', 'is_vendor', 'phone_number', 'address', 'favorite_restaurant', 'restaurant_name', 'restaurant_description', 'restaurant_address']
