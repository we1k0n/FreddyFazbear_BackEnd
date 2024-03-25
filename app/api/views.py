from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    
@api_view(['POST'])
def add_to_cart(request):
    serializer = CartItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_cart(request, user_id):
    cart_items = CartItem.objects.filter(customer_id=user_id)
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)