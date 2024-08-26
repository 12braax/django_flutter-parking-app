from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ParkingSpotViewSet,
    CarRegistrationViewSet,
    UserRegistrationViewSet,
    UserLoginAPIView,
    ForgotPasswordAPIView
)

router = DefaultRouter()
router.register(r'parking_spots', ParkingSpotViewSet)
router.register(r'car_registrations', CarRegistrationViewSet)
router.register(r'user_registrations', UserRegistrationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('forgot-password/', ForgotPasswordAPIView.as_view(), name='forgot-password'),
]