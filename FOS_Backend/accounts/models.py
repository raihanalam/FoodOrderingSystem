from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="user_profile")
     full_name = models.CharField(max_length=264,blank=True)
     profile_pic = models.ImageField(upload_to = 'profile_pics',blank=True)
     description = models.TextField(max_length=264,blank=True)
     dob = models.DateField(blank=True,null=True)
     web = models.URLField(blank=True)
     facebook = models.URLField(blank=True)