# Generated by Django 2.2.4 on 2020-01-29 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200129_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactsfileupload',
            old_name='file_path',
            new_name='csv_file',
        ),
    ]
