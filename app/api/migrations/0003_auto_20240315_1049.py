# Generated by Django 3.2.23 on 2024-03-15 08:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_customeruser_phone_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryuser',
            name='location',
        ),
        migrations.RemoveField(
            model_name='deliveryuser',
            name='time',
        ),
        migrations.AddField(
            model_name='restaurantuser',
            name='closing_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurantuser',
            name='location',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurantuser',
            name='opening_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deliveryuser',
            name='vehicles',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
