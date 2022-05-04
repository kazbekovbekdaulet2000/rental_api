# Generated by Django 4.0.4 on 2022-05-01 17:41

from django.db import migrations, models
import shop.models.image


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_itemimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemimage',
            name='image_thumb10',
        ),
        migrations.RemoveField(
            model_name='itemimage',
            name='image_thumb25',
        ),
        migrations.RemoveField(
            model_name='itemimage',
            name='image_thumb50',
        ),
        migrations.AddField(
            model_name='itemimage',
            name='image_thumb240',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=shop.models.image.thumb_dir, verbose_name='Photo (240px)'),
        ),
        migrations.AddField(
            model_name='itemimage',
            name='image_thumb480',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=shop.models.image.thumb_dir, verbose_name='Photo (480px)'),
        ),
        migrations.AddField(
            model_name='itemimage',
            name='image_thumb720',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=shop.models.image.thumb_dir, verbose_name='Photo (720px)'),
        ),
    ]
