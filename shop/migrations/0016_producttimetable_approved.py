# Generated by Django 4.0.4 on 2022-05-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_producttimetable_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttimetable',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
