from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerUserViewSet, DeliveryUserViewSet, RestaurantUserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'customer-users', CustomerUserViewSet)
router.register(r'delivery-users', DeliveryUserViewSet)
router.register(r'restaurant-users', RestaurantUserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
