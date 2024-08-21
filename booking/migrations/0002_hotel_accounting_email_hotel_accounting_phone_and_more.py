# Generated by Django 5.0.3 on 2024-07-24 12:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='accounting_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='accounting_phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='availabilityandrateprovider',
            field=models.CharField(blank=True, choices=[('ta', 'traveky admin'), ('aa', 'account admin')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='b2b',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='b2c',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='contract_attachement',
            field=models.FileField(null=True, upload_to='contract_attachement', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AddField(
            model_name='hotel',
            name='payment',
            field=models.CharField(blank=True, choices=[('hpg', 'Hotel Payment Geteway'), ('tppg', 'Travky Partner Payment Geteway'), ('tgpg', 'Travky Gartner Payment Geteway')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='reservation_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='reservation_email_phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='sales_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='sales_phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
