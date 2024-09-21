from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(
        max_length=100, blank=True, null=True
    )
    founded_year = models.PositiveIntegerField(
        blank=True, null=True
    )
    website = models.URLField(
        blank=True, null=True
    )
    headquarters = models.CharField(
        max_length=255, blank=True, null=True
    )

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

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
    type = models.CharField(
        max_length=12, choices=CAR_TYPES, default='SUV'
    )
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    engine = models.CharField(
        max_length=50, blank=True, null=True
    )
    transmission = models.CharField(
        max_length=20,
        choices=[('Automatic', 'Automática'), ('Manual', 'Manual')],
        blank=True
    )
    fuel_type = models.CharField(
        max_length=15,
        choices=[
            ('Gasoline', 'Gasolina'),
            ('Diesel', 'Diésel'),
            ('Electric', 'Eléctrico'),
            ('Hybrid', 'Híbrido')
        ],
        blank=True
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
