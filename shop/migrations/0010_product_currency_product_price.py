# Generated by Django 4.0.4 on 2022-05-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_product_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(blank=True, choices=[('T', 'Tenge'), ('EU', 'Euro'), ('USD', 'Dollar')], default='T', max_length=5),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=1000),
        ),
    ]