from django.db import models
from django.core.validators import MaxValueValidator

class Booking(models.Model):
    name = models.CharField(max_length=225)
    no_of_guests = models.IntegerField(validators=[MaxValueValidator(99999999999)])
    booking_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name} for {self.booking_date} '
    
class Menu(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.IntegerField(validators=[MaxValueValidator(99999)])

    def __str__(self):
        return self.title

