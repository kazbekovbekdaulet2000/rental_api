# Generated by Django 4.0.4 on 2022-05-03 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_rename_available_product_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttimetable',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='shop.product'),
        ),
    ]
