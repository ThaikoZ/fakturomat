# Generated by Django 5.0.6 on 2024-06-21 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_rename_frequnecy_template_frequency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='payment_status',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 21, 19, 57, 54, 904071, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_period',
            field=models.DateField(default=datetime.datetime(2024, 6, 28, 19, 57, 54, 905072, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='template',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 21, 19, 57, 54, 905072, tzinfo=datetime.timezone.utc)),
        ),
    ]