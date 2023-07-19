from django.urls import path
from .views import CreateDrone, DronesAvailable, DroneInformation, LoadingDrone, CheckingItems

urlpatterns = [
    path('register-drone/', CreateDrone.as_view(), name='register_drone'),
    path('drones-availables/', DronesAvailable.as_view(), name='drones_available'),
    path('drone-battery/<slug:serial_number>', DroneInformation.as_view(), name='drones_battery'),
    path('loading-drone/', LoadingDrone.as_view(), name='loading_drone'),
    path('checking-items/<slug:serial_number>', CheckingItems.as_view(), name='checking_item'),
]
