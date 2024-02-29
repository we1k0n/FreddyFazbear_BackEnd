from django.contrib import admin
from .models import AdminUser, CustomerUser, DeliveryUser, RestaurantUser, Order, Dish, Cart

admin.site.register(AdminUser)
admin.site.register(CustomerUser)
admin.site.register(DeliveryUser)
admin.site.register(RestaurantUser)
admin.site.register(Order)
admin.site.register(Dish)
admin.site.register(Cart)

