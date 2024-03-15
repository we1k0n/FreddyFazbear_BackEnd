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
    location = models.CharField(max_length=255)
    rate = models.FloatField()
    type = models.CharField(max_length=255)
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()

class Order(models.Model):
    customer_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    delivery_id = models.ForeignKey(DeliveryUser, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(RestaurantUser, on_delete=models.CASCADE)
    cost = models.FloatField()
    rating = models.FloatField()
    time = models.DateTimeField()

class Dish(models.Model):
    restaurant_id = models.ForeignKey(RestaurantUser, on_delete=models.CASCADE)
    cost = models.FloatField()
    count = models.IntegerField()
    type = models.CharField(max_length=255)

class Cart(models.Model):
    customer_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)
    count = models.IntegerField()
