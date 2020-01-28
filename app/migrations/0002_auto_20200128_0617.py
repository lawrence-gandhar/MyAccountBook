# Generated by Django 2.2.3 on 2020-01-28 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='display_name',
            field=models.CharField(blank=True, db_index=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='is_imported_user',
            field=models.BooleanField(blank=True, choices=[(True, 'YES'), (False, 'NO')], db_index=True, default=False),
        ),
    ]
