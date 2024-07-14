# Generated by Django 5.0.3 on 2024-07-13 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0029_update_percent_update_value_alter_updatedetails_val'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('all', 'all periods'), ('c', 'custom periods')], max_length=255)),
                ('val', models.PositiveIntegerField(null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.room')),
            ],
        ),
        migrations.CreateModel(
            name='AvailabilityperoiodsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.availability')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.periods')),
            ],
        ),
        migrations.CreateModel(
            name='Supplement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.PositiveIntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.groups')),
            ],
        ),
    ]
