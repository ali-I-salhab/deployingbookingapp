# Generated by Django 5.0.3 on 2024-07-26 20:14

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_emails_hotel_alter_extraservices_hotel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='contract_attachement',
        ),
        migrations.CreateModel(
            name='ContractAttachement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='contract_attachement', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_Attachment', to='booking.hotel')),
            ],
        ),
    ]
