# Generated by Django 4.0 on 2022-02-01 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeSystem', '0005_feedback_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='passw',
            new_name='password',
        ),
    ]