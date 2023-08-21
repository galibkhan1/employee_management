# Generated by Django 4.0 on 2022-01-25 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('passw', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='signUp',
        ),
    ]
