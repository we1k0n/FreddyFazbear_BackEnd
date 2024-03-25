from django.contrib import admin
from .models import AdminUser, CustomerUser, DeliveryUser, RestaurantUser, Order, Dish,CartItem,OrderItem

admin.site.register(AdminUser)
admin.site.register(CustomerUser)
admin.site.register(DeliveryUser)
admin.site.register(RestaurantUser)
admin.site.register(Order)
admin.site.register(Dish)
admin.site.register(CartItem)
admin.site.register(OrderItem)


