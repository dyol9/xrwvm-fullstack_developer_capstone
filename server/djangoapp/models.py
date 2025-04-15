# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(max_length=100)
    founding_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    dealership_id = models.IntegerField()  
    name = models.CharField(max_length=100)
    
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('PICKUP', 'Pickup'),
        ('VAN', 'Van'),
        ('MINIVAN', 'Minivan'),
        ('CROSSOVER', 'Crossover'),
        ('ELECTRIC', 'Electric'),
        ('HYBRID', 'Hybrid')
    ]
    
    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SUV')
    year = models.DateField()  # Cambiado a DateField según la solicitud
    
    # Campos adicionales
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    engine = models.CharField(max_length=100, blank=True)
    mileage = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="MPG")
    color = models.CharField(max_length=50, blank=True)
    seats = models.PositiveSmallIntegerField(default=5)
    doors = models.PositiveSmallIntegerField(default=4)
    transmission = models.CharField(max_length=20, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.car_make} {self.name} ({self.year.year})" 
