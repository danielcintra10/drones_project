# Generated by Django 4.2.2 on 2023-07-17 21:44

import delivery_company.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.SlugField(max_length=100, unique=True)),
                ('drone_model', models.CharField(choices=[('L', 'Lightweight'), ('M', 'Middleweight'), ('C', 'Cruiserweight'), ('H', 'Heavyweight')], max_length=1)),
                ('weight_limit', models.IntegerField()),
                ('battery_capacity', models.IntegerField(validators=[delivery_company.validators.validate_battery_capacity])),
                ('state', models.CharField(choices=[('IDL', 'IDLE'), ('LDG', 'LOADING'), ('LDD', 'LOADED'), ('DLG', 'DELIVERING'), ('DLD', 'DELIVERED'), ('RTG', 'RETURNING')], max_length=3)),
            ],
        ),
    ]
