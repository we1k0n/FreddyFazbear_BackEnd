# Generated by Django 3.2.23 on 2024-03-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20240319_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
