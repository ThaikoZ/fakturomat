# Generated by Django 5.0.6 on 2024-06-21 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_invoice_details_invoice_payments_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 21, 16, 22, 56, 767214, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payments_period',
            field=models.DateField(default=datetime.datetime(2024, 6, 28, 16, 22, 56, 767214, tzinfo=datetime.timezone.utc)),
        ),
    ]