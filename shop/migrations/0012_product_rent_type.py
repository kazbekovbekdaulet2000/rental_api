# Generated by Django 4.0.4 on 2022-05-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_rename_free_product_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rent_type',
            field=models.CharField(blank=True, choices=[('hourly', 'for hours'), ('daily', 'for days'), ('weekly', 'for weeks'), ('monthly', 'for months'), ('yearly', 'for years')], default='hourly', max_length=16),
        ),
    ]