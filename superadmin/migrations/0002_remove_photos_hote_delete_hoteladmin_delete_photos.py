# Generated by Django 5.0.3 on 2024-06-27 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='hote',
        ),
        migrations.DeleteModel(
            name='HotelAdmin',
        ),
        migrations.DeleteModel(
            name='photos',
        ),
    ]