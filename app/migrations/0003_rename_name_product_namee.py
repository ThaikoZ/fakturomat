# Generated by Django 5.0.6 on 2024-06-20 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_invoiceitem_invoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='namee',
        ),
    ]