# Generated by Django 2.2.3 on 2019-12-18 20:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0017_profile_app_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Addresses',
            new_name='User_Address_Details',
        ),
    ]
