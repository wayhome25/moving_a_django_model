from django.contrib import admin

from cars.models import Car, Tires


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'tires_name')

    def tires_name(self, obj):
        return obj.tires.name


@admin.register(Tires)
class TiresAdmin(admin.ModelAdmin):
    list_display = ('name', 'size')
