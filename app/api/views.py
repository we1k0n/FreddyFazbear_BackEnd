from rest_framework import viewsets
from .models import CustomerUser, DeliveryUser, RestaurantUser
from .serializers import CustomerUserSerializer, DeliveryUserSerializer, RestaurantUserSerializer

class CustomerUserViewSet(viewsets.ModelViewSet):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer

class DeliveryUserViewSet(viewsets.ModelViewSet):
    queryset = DeliveryUser.objects.all()
    serializer_class = DeliveryUserSerializer

class RestaurantUserViewSet(viewsets.ModelViewSet):
    queryset = RestaurantUser.objects.all()
    serializer_class = RestaurantUserSerializer
