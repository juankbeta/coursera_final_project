from django.contrib import admin
from .models import CarMake, CarModel


class CarModelAdmin(admin.ModelAdmin):
    fields = ['car_make', 'name', 'type', 'year', 'engine']


class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5


class CarMakeAdmin(admin.ModelAdmin):
    fields = [
        'name', 'description', 'country_of_origin', 'founded_year', 'website'
    ]
    inlines = [CarModelInline]


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
