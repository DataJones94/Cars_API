# Generated by Django 4.1.6 on 2023-02-17 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealerships', '0001_initial'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='dealership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dealerships.dealership'),
        ),
    ]
