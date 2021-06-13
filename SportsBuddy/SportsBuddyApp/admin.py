from django.contrib import admin
from .models import Sport, Event, UserProfile
# Register your models here.
admin.site.register(Sport)
admin.site.register(Event)
admin.site.register(UserProfile)
