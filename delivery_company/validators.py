from django.core.exceptions import ValidationError
import re


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
