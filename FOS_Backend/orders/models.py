from django.db import models
from django.contrib.auth.models import User
from kitchen.models import Item

# Create your models here.
class Cart(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
     item = models.ForeignKey(Item,on_delete=models.CASCADE)
     quantity = models.IntegerField(default=1)
     purchased = models.BooleanField(default=False)
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)

     def __str__(self):
          return f'{self.quantity} x {self.item}'

     def get_total(self):
          total = self.item.price * self.quantity
          float_total = format(total, '0.2f')
          return float_total

class Order(models.Model):
     orderitems = models.ManyToManyField(Cart)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     ordered = models.BooleanField(default=False)
     created = models.DateTimeField(auto_now_add=True)
     paymentId = models.CharField(max_length=264, blank=True, null=True) 
     orderId = models.CharField(max_length=200, blank=True, null=True)

     def get_totals(self):
          total = 0
          for order_item in self.orderitems.all():
               total += float(order_item.get_total())
          return total
     


# Create your models here.
class BillingAddress(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='payment')
     address = models.CharField(max_length=300,blank=True)
     city = models.CharField(max_length=40,blank=True)
     zipcode = models.CharField(max_length=10,blank=True)
     country = models.CharField(max_length=50,blank=True)
     
     def __str__(self):
          return f'{self.user.profile.username} billing address'

     def is_fully_filled(self):
          fields_names = [f.name for f in self._meta.get_fields()]

          for field_name in fields_names:
               value = getattr(self,field_name)
               if value is None or value=='':
                    return False
          return True 

     class Meta:
          verbose_name_plural = "Billing Addresses"