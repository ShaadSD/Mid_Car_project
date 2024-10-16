# Generated by Django 5.0.6 on 2024-10-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(default='No description available.'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='cars'),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='car',
            name='title',
            field=models.CharField(default='Untitled', max_length=50),
        ),
    ]
