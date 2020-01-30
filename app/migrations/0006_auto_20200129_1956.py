# Generated by Django 2.2.3 on 2020-01-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200129_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='is_msme_reg',
            field=models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=False),
        ),
        migrations.AddField(
            model_name='contacts',
            name='is_sub_customer',
            field=models.IntegerField(blank=True, choices=[(1, 'Parent Customer'), (2, 'Bill With Parent'), (3, 'Bill with Customer')], db_index=True, default=1, null=True),
        ),
    ]