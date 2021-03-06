# Generated by Django 2.2.4 on 2020-03-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_user_address_details_is_billing_address_diff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_address_details',
            name='is_billing_address',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name='user_address_details',
            name='is_shipping_address',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=False),
        ),
    ]
