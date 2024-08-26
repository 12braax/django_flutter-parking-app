from django.db import models

class ParkingSpot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.IntegerField()

    def __str__(self):
        return f"ID:{self.id}: From {self.start_time} To {self.end_time}, Price: {self.price} Birr"

class CarRegistration(models.Model):
    car_model = models.CharField(max_length=100)
    car_plate = models.CharField(max_length=17)  # Updated field
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Car Registration - {self.car_plate}"

class UserRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"User Registration - {self.name}"
