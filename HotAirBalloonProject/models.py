from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Balloon(models.Model):
    BALLOON_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("V", "VIP")
    ]

    type = models.CharField(max_length=1, choices=BALLOON_CHOICES)
    manufacturer = models.CharField(max_length=50)
    max_passengers = models.IntegerField()

    def __str__(self):
        return self.type + ' ' + self.manufacturer + ' ' + self.max_passengers.__str__()


class Airline(models.Model):
    name = models.CharField(max_length=50)
    year_founded = models.PositiveIntegerField()
    flights_outside_europe = models.BooleanField()

    def __str__(self):
        return self.name


class Pilot(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    total_flight_hours = models.IntegerField()
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.last_name


class Flight(models.Model):
    code = models.CharField(max_length=50)
    airport_to = models.CharField(max_length=50)
    airport_from = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return self.code + ' ' + self.airport_from + ' ' + self.airport_to + ' '


class AirlinePilots(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return self.pilot.__str__() + ' ' + self.airline.__str__()
