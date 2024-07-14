# Generated by Django 5.0.3 on 2024-07-13 04:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0026_alter_bedoptiondetails_room_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('f', 'fixed'), ('r', 'related'), ('p', 'percent')], max_length=255)),
                ('u_tupe', models.CharField(choices=[('u', 'update'), ('d', 'downgrade')], max_length=255)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.groups')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.hotel')),
                ('mealplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.mealplan')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.periods')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.room')),
            ],
        ),
    ]