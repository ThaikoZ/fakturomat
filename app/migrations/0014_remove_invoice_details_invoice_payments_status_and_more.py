# Generated by Django 5.0.6 on 2024-06-21 16:21

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_product_price_product_unit_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='details',
        ),
        migrations.AddField(
            model_name='invoice',
            name='payments_status',
            field=models.CharField(choices=[('UNPAID', 'Unpaid'), ('PAID', 'Paid'), ('CANCELLED', 'Cancelled')], default='UNPAID', max_length=255),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.client'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 21, 18, 21, 32, 999438)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payments_method',
            field=models.CharField(choices=[('CASH', 'In Cash'), ('DEBIT', 'Debit Card'), ('CREDIT', 'Credit Card'), ('PAYPAL', 'PayPal')], default='CREDIT', max_length=255),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payments_period',
            field=models.DateField(default=datetime.datetime(2024, 6, 28, 18, 21, 32, 999438)),
        ),
    ]
