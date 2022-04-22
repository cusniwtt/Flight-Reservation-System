# Create your models here.
from django.db import models
from datetime import datetime

from django.utils import timezone


# Create your models here.

class Flight(models.Model):
    flight_name = models.CharField(max_length=30, null=True)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=6)
    rem = models.DecimalField(decimal_places=0, max_digits=6)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField(default = timezone.now)
    time = models.TimeField(default = timezone.now)
    date1 = models.DateField(default = timezone.now)
    time1 = models.TimeField(default = timezone.now)

    def __str__(self):
        return self.flight_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    flightid=models.DecimalField(decimal_places=0, max_digits=2)
    flight_name = models.CharField(max_length=30, null=True)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=6)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField(default = timezone.now)
    time = models.TimeField(default = timezone.now)
    date1 = models.DateField(default = timezone.now)
    time1 = models.TimeField(default = timezone.now)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=255)

    def __str__(self):
        return self.email
