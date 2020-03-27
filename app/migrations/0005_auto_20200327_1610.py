# Generated by Django 2.2.4 on 2020-03-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user_address_details_is_billing_address_diff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryproduct',
            name='min_hold_notify_trigger',
            field=models.FloatField(blank=True, choices=[(0, '5 DAYS AGO'), (1, '1 WEEK AGO'), (2, '10 DAYS AGO'), (3, '2 WEEKS AGO'), (4, '1 MONTH AGO'), (5, '45 DAYS AGO'), (6, '2 MONTHS AGO'), (7, '3 MONTHS AGO'), (8, '6 MONTHS AGO'), (9, '1 YEAR AGO')], db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryproduct',
            name='quantity',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='inventoryproduct',
            name='stop_at_min_hold',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='inventoryproduct',
            name='threshold',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='adjustment',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='discount',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='shipping',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='subtotal',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='subtotal_inc_tax',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='total',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='abatement',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='cost_price',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='discount',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='gst',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='marked_price',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='selling_price',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='tax',
            field=models.FloatField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='user_account_details',
            name='account_number',
            field=models.IntegerField(blank=True, db_index=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user_tax_details',
            name='opening_balance',
            field=models.FloatField(blank=True, db_index=True, default=0.0, null=True),
        ),
    ]
