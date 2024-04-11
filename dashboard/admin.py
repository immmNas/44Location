from django.contrib import admin
from .models import Customer, Reservation, Car
# Register your models here.


admin.site.register(Customer)
admin.site.register(Reservation)
admin.site.register(Car)
