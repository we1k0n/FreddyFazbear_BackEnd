from django.contrib.auth.models import User
from django.db import models

class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Додаткові поля для адміністратора

class CustomerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Додаткові поля для звичайного користувача

class DeliveryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicles = models.CharField(max_length=255,null=True, blank=True)
    active_order_id = models.IntegerField()
    phone_num = models.CharField(max_length=20)
    # Додаткові поля для доставка

class RestaurantUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.FloatField()
    type = models.CharField(max_length=255)
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='restaurant_photos', null=True, blank=True)

class Order(models.Model):
    customer_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    delivery_id = models.ForeignKey(DeliveryUser, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(RestaurantUser, on_delete=models.CASCADE)
    cost = models.FloatField()
    time = models.DateTimeField()  
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)

class Dish(models.Model):
    restaurant_id = models.ForeignKey(RestaurantUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cost = models.FloatField()
    type = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='dish_photos', null=True, blank=True)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Cart(models.Model):
    customer_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    count = models.IntegerField()

class CartItem(models.Model):
    order = models.ForeignKey(Order, related_name='cart_items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField()
