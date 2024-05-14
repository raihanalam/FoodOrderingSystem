from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
     name = models.CharField(max_length=30, verbose_name='Category Name')

     def __str__(self):
        return self.name

class Menu(models.Model):
     name = models.CharField(max_length=30, verbose_name='Menu Name')
     image = models.ImageField(upload_to='menu_images')

     def __str__(self):
        return self.name

class Kitchen(models.Model):
     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kitchens')
     name = models.CharField(max_length=30, verbose_name='Kitchen Name')
     address = models.CharField(max_length=50, verbose_name='Address')
     city = models.CharField(max_length=20, verbose_name='City')
     cooking_time = models.IntegerField(default=0, verbose_name='Cooking Time')
     delivery_charge = models.DecimalField(default=0,  verbose_name='Delivery Charge')
     ratings = models.DecimalField(default=0, verbose_name='Ratings')
     created_date = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.name

class Item(models.Model):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name='items')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100, verbose_name='Item Name')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.name
