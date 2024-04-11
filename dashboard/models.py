from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    CARBURANT = (
        ('Diesel', 'Diesel'),
        ('Hybride', 'Hybride'),
        ('Essence', 'Essence'),
        ('Electrique', 'Electrique'),
    )
    TRANSMISSION = (
        ('Manuelle', 'Manuelle'),
        ('Automatique', 'Automatique'),
    )
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    max_speed = models.CharField(max_length=200)
    description = models.TextField()
    buy_date = models.DateField(null=True, blank=True)
    transmission = models.CharField(max_length=200, null=True, blank=True, choices=TRANSMISSION)
    carburant = models.CharField(max_length=200, null=True, blank=True, choices=CARBURANT)
    consumption = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.brand


class Reservation(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('In progress', 'In progress'),
        ('Ended', 'Ended'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    car = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

