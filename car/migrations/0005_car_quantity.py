# Generated by Django 5.0.6 on 2024-10-04 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_alter_car_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
