from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerUserViewSet, DeliveryUserCreateView, DeliveryUserViewSet, RestaurantUserCreateView, RestaurantUserViewSet,CustomerUserCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'customer-users', CustomerUserViewSet)
router.register(r'delivery-users', DeliveryUserViewSet)
router.register(r'restaurant-users', RestaurantUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/customer', CustomerUserCreateView.as_view(), name='register_customer'),
    path('register/delivery/', DeliveryUserCreateView.as_view(), name='register_delivery'),
    path('register/restaurant/', RestaurantUserCreateView.as_view(), name='register_restaurant'),
]
