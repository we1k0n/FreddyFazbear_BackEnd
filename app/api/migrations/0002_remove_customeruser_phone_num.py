# Generated by Django 3.2.23 on 2024-03-01 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeruser',
            name='phone_num',
        ),
    ]