# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)  # País de origen de la marca
    founded_year = models.PositiveIntegerField(blank=True, null=True)  # Año de fundación de la marca
    website = models.URLField(blank=True, null=True)  # Sitio web oficial de la marca
    headquarters = models.CharField(max_length=255, blank=True, null=True)  # Sede principal de la marca

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Relación Many-to-One con CarMake
    name = models.CharField(max_length=100)  # Nombre del modelo de carro
    # Tipos de carro
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('HATCHBACK', 'Hatchback'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
        ('SPORT', 'Sport'),
        ('ELECTRIC', 'Electric'),
    ]
    type = models.CharField(max_length=12, choices=CAR_TYPES, default='SUV')  # Tipo de carro
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    
    # Atributos adicionales
    engine = models.CharField(max_length=50, blank=True, null=True)  # Tipo de motor
    transmission = models.CharField(max_length=20, choices=[('Automatic', 'Automática'), ('Manual', 'Manual')], blank=True, null=True)  # Tipo de transmisión
    fuel_type = models.CharField(max_length=15, choices=[('Gasoline', 'Gasolina'), ('Diesel', 'Diésel'), ('Electric', 'Eléctrico'), ('Hybrid', 'Híbrido')], blank=True, null=True)  # Tipo de combustible
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Precio del modelo

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
