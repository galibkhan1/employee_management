# Generated by Django 4.0 on 2022-01-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeSystem', '0002_registration_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
    ]
