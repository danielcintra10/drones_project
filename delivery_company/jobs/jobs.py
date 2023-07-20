from delivery_company.models import BatteryLog, Drone


def battery_log():
    drones = Drone.objects.all()
    drone_list = []
    if drones:
        for drone in drones:
            battery = drone.battery_capacity
            new_log = BatteryLog(drone=drone, battery_level=battery)
            drone_list.append(new_log)
        log = BatteryLog.objects.bulk_create(drone_list)


