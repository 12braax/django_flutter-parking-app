from django.core.mail import send_mail
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.hashers import make_password
from .models import ParkingSpot, CarRegistration, UserRegistration
from .serializers import (
    ParkingSpotSerializer,
    CarRegistrationSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer,
    ForgotPasswordSerializer
)

User = get_user_model()

class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer


class CarRegistrationViewSet(viewsets.ModelViewSet):
    queryset = CarRegistration.objects.all()
    serializer_class = CarRegistrationSerializer


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer
 

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email').strip().lower()  # Normalize email

            user = User.objects.filter(email__iexact=email).first()  # Case-insensitive search
            if user is None:
                return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

            password = serializer.validated_data.get('password')

            if not user.check_password(password):
                return Response({'error': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)

            # Implement your login logic here
            # Example: Generate JWT token, set session, etc.
            # Return appropriate response if authentication is successful
            return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')

            try:
                user = User.objects.get(email=email)
                # Generate a password reset token here and send it to the user's email
                # Example: password_reset_token = generate_token()
                # user.password_reset_token = password_reset_token
                # user.save()

                # Send an email with the password reset instructions
                send_mail(
                    'Password Reset Request',
                    f'Please use this token to reset your password: <password_reset_token>',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )

                return Response({'message': 'Password reset instructions have been sent to your email.'})
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
