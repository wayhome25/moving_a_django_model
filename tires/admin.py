from django.contrib import admin

# Register your models here.
from tires.models import Tires


@admin.register(Tires)
class TiresAdmin(admin.ModelAdmin):
    list_display = ('name', 'size')
