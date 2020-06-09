from django.contrib import admin

from .models import Bed, Plant, Event


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'origin')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('type', 'bed', 'plant', 'count', 'datetime')


admin.site.register(Bed)
