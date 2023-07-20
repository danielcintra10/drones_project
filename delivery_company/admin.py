from django.contrib import admin
from .models import Drone, Medication, Order, LoadItem, BatteryLog

# Register your models here.
admin.site.register(Drone)
admin.site.register(Medication)
admin.site.register(Order)
admin.site.register(LoadItem)


class BatteryLogAdmin(admin.ModelAdmin):
    list_display = ('drone', 'battery_level', 'date')
    readonly_fields = ('drone', 'battery_level', 'date')


admin.site.register(BatteryLog, BatteryLogAdmin)
