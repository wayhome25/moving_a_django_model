from django.contrib import admin

from cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'tires_name')

    def tires_name(self, obj):
        return obj.tires.name
