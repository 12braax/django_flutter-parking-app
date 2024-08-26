from django.contrib import admin
from .models import ParkingSpot, CarRegistration,UserRegistration
admin.site.register(ParkingSpot)
admin.site.register(CarRegistration)
admin.site.register(UserRegistration)
admin.site.site_header = "Bole Car Parking"
admin.site.site_title = "Admin"
admin.site.index_title = "Admin Role"