from rest_framework import viewsets
from .models import CustomerUser, DeliveryUser, RestaurantUser
from .serializers import CustomerUserSerializer, DeliveryUserSerializer, RestaurantUserSerializer
from rest_framework import generics

class CustomerUserViewSet(viewsets.ModelViewSet):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer

class DeliveryUserViewSet(viewsets.ModelViewSet):
    queryset = DeliveryUser.objects.all()
    serializer_class = DeliveryUserSerializer

class RestaurantUserViewSet(viewsets.ModelViewSet):
    queryset = RestaurantUser.objects.all()
    serializer_class = RestaurantUserSerializer

class CustomerUserCreateView(generics.CreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer
    
class DeliveryUserCreateView(generics.CreateAPIView):
    queryset = DeliveryUser.objects.all()
    serializer_class = DeliveryUserSerializer
    
class RestaurantUserCreateView(generics.CreateAPIView):
    queryset = RestaurantUser.objects.all()
    serializer_class = RestaurantUserSerializer