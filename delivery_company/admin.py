from django.contrib import admin
from .models import Drone, Medication, Order, LoadItem

# Register your models here.
admin.site.register(Drone)
admin.site.register(Medication)
admin.site.register(Order)
admin.site.register(LoadItem)

