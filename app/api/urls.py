from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'customer-users', CustomerUserViewSet)
router.register(r'delivery-users', DeliveryUserViewSet)
router.register(r'restaurant-users', RestaurantUserViewSet)
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'order_items', OrderItemViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart_items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/customer', CustomerUserCreateView.as_view(), name='register_customer'),
    path('register/delivery/', DeliveryUserCreateView.as_view(), name='register_delivery'),
    path('register/restaurant/', RestaurantUserCreateView.as_view(), name='register_restaurant'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('user-cart/<int:user_id>/', user_cart, name='user_cart'),
]

