# Generated by Django 5.0.3 on 2024-07-04 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_hotel_category_alter_hotel_hotestars_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='logo',
            field=models.ImageField(default=1, upload_to='hotel/logos'),
            preserve_default=False,
        ),
    ]