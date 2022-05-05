# Generated by Django 4.0.4 on 2022-05-05 01:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.PositiveIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
