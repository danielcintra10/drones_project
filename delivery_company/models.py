from django.db import models
from django.core.exceptions import ValidationError
from .utils import drone_states, drone_models
from .validators import validate_battery_capacity, validate_medication_code, validate_medication_name, \
    validate_load_quantity, validate_weight_limit


# Create your models here.
class Drone(models.Model):
    serial_number = models.SlugField(max_length=100, unique=True)
    drone_model = models.CharField(max_length=1, choices=drone_models)
    weight_limit = models.IntegerField(validators=[validate_weight_limit, ])
    battery_capacity = models.IntegerField(validators=[validate_battery_capacity, ])
    state = models.CharField(max_length=3, choices=drone_states)

    def __str__(self):
        return self.serial_number

    def clean(self):
        match self.drone_model:
            case 'L':
                if not 0 <= self.weight_limit <= 125:
                    raise ValidationError(
                        f"In case of this drone {self.get_drone_model_display()}, "
                        f"weight possible range is since 0 to 125, {self.weight_limit} is out of this range",
                    )
            case 'M':
                if not 126 <= self.weight_limit <= 250:
                    raise ValidationError(
                        f"In case of this drone {self.get_drone_model_display()}, "
                        f"weight possible range is since 126 to 250, {self.weight_limit} is out of this range",
                    )
            case 'C':
                if not 251 <= self.weight_limit <= 375:
                    raise ValidationError(
                        f"In case of this drone {self.get_drone_model_display()}, "
                        f"weight possible range is since 251 to 375, {self.weight_limit} is out of this range",
                    )
            case 'H':
                if not 376 <= self.weight_limit <= 500:
                    raise ValidationError(
                        f"In case of this drone {self.get_drone_model_display()}, "
                        f"weight possible range is since 376 to 500, {self.weight_limit} is out of this range",
                    )


class Medication(models.Model):
    code = models.SlugField(unique=True, validators=[validate_medication_code, ])
    name = models.CharField(max_length=50, validators=[validate_medication_name, ])
    weight = models.IntegerField()
    image = models.ImageField(upload_to='medication_images', blank=True, null=True)

    def __str__(self):
        return self.code


class Order(models.Model):
    order_code = models.SlugField(max_length=50, unique=True)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_code


class LoadItem(models.Model):
    order_code = models.ForeignKey(Order, related_name='load_items', on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[validate_load_quantity, ], default=1)

    def __str__(self):
        return f"{self.order_code}, {self.medication}, {self.medication}"
