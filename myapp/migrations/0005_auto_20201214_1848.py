# Generated by Django 3.1.4 on 2020-12-14 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_book_flight_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bus_name',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='bus_name',
        ),
    ]
