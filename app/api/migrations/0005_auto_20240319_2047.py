# Generated by Django 3.2.23 on 2024-03-19 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20240319_2045'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='Item',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='dish_id',
        ),
    ]
