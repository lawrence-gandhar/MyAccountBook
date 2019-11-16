# Generated by Django 2.2.4 on 2019-11-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_invoice_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_addresses',
            name='same_billing_shipping_address',
        ),
        migrations.AddField(
            model_name='contact_addresses',
            name='city',
            field=models.CharField(db_index=True, default='default', max_length=250),
        ),
        migrations.AddField(
            model_name='contact_addresses',
            name='country',
            field=models.CharField(db_index=True, default='default', max_length=250),
        ),
        migrations.AddField(
            model_name='contact_addresses',
            name='flat_no',
            field=models.CharField(db_index=True, default='default', max_length=250),
        ),
        migrations.AddField(
            model_name='contact_addresses',
            name='pincode',
            field=models.CharField(db_index=True, default='default', max_length=250),
        ),
        migrations.AddField(
            model_name='contact_addresses',
            name='state',
            field=models.CharField(db_index=True, default='default', max_length=250),
        ),
        migrations.AddField(
            model_name='contact_addresses',
            name='street',
            field=models.CharField(db_index=True, default='default', max_length=250),
        ),
    ]
