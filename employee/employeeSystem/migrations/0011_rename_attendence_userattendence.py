# Generated by Django 4.0 on 2022-02-08 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeSystem', '0010_rename_user_attendence_attendence_attendence'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='attendence',
            new_name='userattendence',
        ),
    ]
