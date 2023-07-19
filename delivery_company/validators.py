from django.core.exceptions import ValidationError
import re
from rest_framework import serializers


def validate_battery_capacity(value):
    if not 0 <= value <= 100:
        raise ValidationError(
            f"{value} battery needs to be between 0 and 100",
        )


def validate_medication_code(value):
    if re.findall(r'[a-z ()\[\]{}|\\`~!@#$%^&*+=;\-:\'",<>./?]', value):
        raise ValidationError(
            f"{value} medication code only allow upper case letters, underscore and numbers",
        )


def validate_medication_name(value):
    if re.findall(r'[()\[\]{}|\\`~!@#$%^&*+=;:\'",<>./?]', value):
        raise ValidationError(
            f"{value} medication name only allow letters, numbers, ‘-‘, ‘_’",
        )


def validate_load_quantity(value):
    if not value > 0:
        raise ValidationError(
            f"{value} quantity needs to be greater than 0",
        )


def validate_weight_limit(value):
    if not value > 0:
        raise ValidationError(
            f"{value} weight limit needs to be greater than 0",
        )


def validate_drone_weight_limit(drone_model, weight_limit):
    match drone_model:
        case 'L':
            if not 0 <= weight_limit <= 125:
                raise serializers.ValidationError(
                    f"In case of this drone model Lightweight, "
                    f"weight possible range is since 0 to 125, {weight_limit} is out of this range",
                )
        case 'M':
            if not 126 <= weight_limit <= 250:
                raise serializers.ValidationError(
                    f"In case of this drone Middleweight, "
                    f"weight possible range is since 126 to 250, {weight_limit} is out of this range",
                )
        case 'C':
            if not 251 <= weight_limit <= 375:
                raise serializers.ValidationError(
                    f"In case of this drone Cruiserweight, "
                    f"weight possible range is since 251 to 375, {weight_limit} is out of this range",
                )
        case 'H':
            if not 376 <= weight_limit <= 500:
                raise serializers.ValidationError(
                    f"In case of this drone Heavyweight, "
                    f"weight possible range is since 376 to 500, {weight_limit} is out of this range",
                )
