# Generated by Django 5.1 on 2024-08-16 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ParkingSystem', '0004_userregistration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carregistration',
            name='reservation_end_time',
        ),
        migrations.RemoveField(
            model_name='carregistration',
            name='reservation_start_time',
        ),
    ]