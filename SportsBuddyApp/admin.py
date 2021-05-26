from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Sport, Event
# Register your models here.
admin.site.register(Sport)
admin.site.register(Event)


class EventAdmin(OSMGeoAdmin):
    list_display = ('location')
