from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import ParkingSpot, CarRegistration, UserRegistration

User = get_user_model()

class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = ['id', 'start_time', 'end_time', 'price']


class CarRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRegistration
        fields = ['id', 'name', 'phone_number', 'email', 'car_model', 'vin', 'parking_spot']


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['name', 'email', 'password']

    def create(self, validated_data):
        # Manually hash the password
        user = UserRegistration(
            name=validated_data['name'],
            email=validated_data['email'].strip().lower(),  # Normalize email
        )
        user.password = make_password(validated_data['password'])  # Hash the password
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user found with this email address.")
        return value
