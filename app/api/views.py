from rest_framework import viewsets
from .models import *
from .serializers import *
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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer