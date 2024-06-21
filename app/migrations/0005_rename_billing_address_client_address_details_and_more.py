# Generated by Django 5.0.6 on 2024-06-21 07:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_namee_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='billing_address',
            new_name='address_details',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='phone',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='invoiceitem',
            old_name='price',
            new_name='VAT',
        ),
        migrations.RenameField(
            model_name='invoiceitem',
            old_name='quantity',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='client',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='client',
            name='shipping_address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AddField(
            model_name='client',
            name='payments_method',
            field=models.CharField(choices=[('PAYPAL', 'PayPay'), ('CREDITCARD', 'Credit Card'), ('CASH', 'Cash'), ('DEBITCARD', 'Debit Card')], default='CASH', max_length=20),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payments_period',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(db_column='client_id', on_delete=django.db.models.deletion.PROTECT, to='app.client'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('UNPAID', 'Unpaid'), ('PAID', 'Paid'), ('CANCELLED', 'Cancelled')], default='UNPAID', max_length=20),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='invoice',
            field=models.ForeignKey(db_column='invoice_id', on_delete=django.db.models.deletion.PROTECT, to='app.invoice'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='product',
            field=models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.PROTECT, to='app.product'),
        ),
        migrations.AlterModelTable(
            name='client',
            table='client',
        ),
        migrations.AlterModelTable(
            name='invoice',
            table='invoice',
        ),
        migrations.AlterModelTable(
            name='invoiceitem',
            table='products_in_invoice',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('details', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('client', models.ForeignKey(db_column='client_id', on_delete=django.db.models.deletion.PROTECT, to='app.client')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('VAT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.PROTECT, to='app.product')),
                ('template', models.ForeignKey(db_column='template_id', on_delete=django.db.models.deletion.PROTECT, to='app.template')),
            ],
            options={
                'db_table': 'products_in_template',
            },
        ),
    ]