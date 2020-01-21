# Generated by Django 2.2.3 on 2020-01-20 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200121_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice_templates',
            name='user_custom_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='invoice_templates',
            name='user_email',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='invoice_templates',
            name='user_phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='invoice_templates',
            name='user_display_name',
            field=models.BooleanField(choices=[(True, 'USE USER FIRSTNAME LASTNAME'), (False, 'USE CUSTOM USERNAME')], db_index=True, default=True),
        ),
    ]