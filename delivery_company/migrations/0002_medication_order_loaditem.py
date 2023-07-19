# Generated by Django 4.2.2 on 2023-07-19 12:02

import delivery_company.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(unique=True, validators=[delivery_company.validators.validate_medication_code])),
                ('name', models.CharField(max_length=50, validators=[delivery_company.validators.validate_medication_name])),
                ('weight', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='medication_images')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.SlugField(unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery_company.drone')),
            ],
        ),
        migrations.CreateModel(
            name='LoadItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, validators=[delivery_company.validators.validate_load_quantity])),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery_company.medication')),
                ('order_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='load_items', to='delivery_company.order')),
            ],
        ),
    ]
