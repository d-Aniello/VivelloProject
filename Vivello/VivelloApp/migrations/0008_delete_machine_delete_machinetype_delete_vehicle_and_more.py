# Generated by Django 4.0.3 on 2022-03-06 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VivelloApp', '0007_crop'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Machine',
        ),
        migrations.DeleteModel(
            name='MachineType',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
        migrations.DeleteModel(
            name='VehicleType',
        ),
    ]
