# Generated by Django 2.2.3 on 2020-01-24 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200123_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='as_of',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='business_reg_no',
            field=models.CharField(blank=True, db_index=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='cst_reg_no',
            field=models.CharField(blank=True, db_index=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='gst_reg_type',
            field=models.IntegerField(choices=[(0, 'Not Applicable'), (1, 'GST Registered-Regular'), (2, 'GST Registered-Composition,'), (3, 'GST unregistered'), (4, 'Consumer'), (5, 'Overseas'), (6, 'SEZ'), (7, 'Deemed Exports -EOU’s, STP’s , EHTP’s etc')], db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='contacts',
            name='opening_balance',
            field=models.IntegerField(blank=True, db_index=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='organization_name',
            field=models.CharField(blank=True, db_index=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='organization_type',
            field=models.IntegerField(db_index=True, default=1),
        ),
        migrations.AddField(
            model_name='contacts',
            name='preferred_currency',
            field=models.IntegerField(blank=True, choices=[(0, 'ANY'), (1, 'RUPEES'), (2, 'USD'), (3, 'EURO'), (4, 'Pound')], db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='preferred_delivery',
            field=models.IntegerField(blank=True, choices=[(0, 'None'), (1, 'Print later'), (2, 'Send Later')], db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='preferred_payment_method',
            field=models.IntegerField(blank=True, choices=[(0, 'Any'), (1, 'Cash'), (2, 'Card'), (3, 'Cheque'), (4, 'Net banking')], db_index=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='tax_reg_no',
            field=models.CharField(blank=True, db_index=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='contact_addresses',
            name='is_billing_address',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='contact_addresses',
            name='is_shipping_address',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='contacts_email',
            name='is_official',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name='contacts_email',
            name='is_personal',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=True),
        ),
    ]
