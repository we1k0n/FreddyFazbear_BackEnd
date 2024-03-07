from rest_framework import serializers
from .models import CustomerUser, DeliveryUser, RestaurantUser

class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = '__all__'

class DeliveryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryUser
        fields = '__all__'

class RestaurantUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantUser
        fields = '__all__'

