# Generated by Django 4.0.4 on 2022-05-03 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_producttime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='available',
            new_name='active',
        ),
    ]
