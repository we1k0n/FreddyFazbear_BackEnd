from rest_framework import serializers
from .models import CustomerUser, DeliveryUser, RestaurantUser
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class CustomerUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CustomerUser
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        customer_user = CustomerUser.objects.create(user=user, **validated_data)
        return customer_user

class DeliveryUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = DeliveryUser
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        delivery_user = DeliveryUser.objects.create(user=user, **validated_data)
        return delivery_user

class RestaurantUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantUser
        fields = '__all__'

