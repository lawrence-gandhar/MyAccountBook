# Generated by Django 2.2.3 on 2020-01-20 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200121_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice_templates',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.User_Address_Details'),
        ),
    ]