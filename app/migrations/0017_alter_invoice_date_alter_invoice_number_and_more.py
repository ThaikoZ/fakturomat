# Generated by Django 5.0.6 on 2024-06-21 18:28

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_payments_method_invoice_payment_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 21, 18, 28, 10, 493868, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.CharField(max_length=55, unique=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_period',
            field=models.DateField(default=datetime.datetime(2024, 6, 28, 18, 28, 10, 493868, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_status',
            field=models.CharField(choices=[('UNPAID', 'Unpaid'), ('PAID', 'Paid')], default='UNPAID', max_length=255),
        ),
        migrations.AlterField(
            model_name='productininvoice',
            name='VAT',
            field=models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='productininvoice',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='productintemplate',
            name='VAT',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
