from django.db import models

# Django database model
class Flight(models.Model):
    flightNumber = models.CharField(max_length=7, primary_key=True)
    departureAirport = models.CharField(max_length=10)
    arrivalAirport = models.CharField(max_length=10)
    flightDate = models.IntegerField()    
    aircraft = models.CharField(max_length=10)
    paxAvailable = models.IntegerField()
    paxBooked = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)