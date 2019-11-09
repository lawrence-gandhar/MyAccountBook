# Generated by Django 2.2.3 on 2019-11-09 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20191109_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='is_customer',
            field=models.BooleanField(blank=True, choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=False, null=True),
        ),
    ]
