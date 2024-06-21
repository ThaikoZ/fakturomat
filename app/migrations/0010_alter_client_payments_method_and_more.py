# Generated by Django 5.0.6 on 2024-06-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_invoice_payments_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='payments_method',
            field=models.CharField(choices=[('UNPAID', 'Unpaid'), ('PAID', 'Paid'), ('CANCELLED', 'Cancelled')], default='UNPAID', max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
