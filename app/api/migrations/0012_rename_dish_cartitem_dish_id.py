# Generated by Django 3.2.23 on 2024-03-25 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20240325_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='dish',
            new_name='dish_id',
        ),
    ]