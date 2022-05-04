# Generated by Django 4.0.4 on 2022-05-01 17:23

from django.db import migrations, models
import django.db.models.deletion
import shop.models.image


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to=shop.models.image.product_dir, verbose_name='Photo')),
                ('image_thumb10', models.ImageField(blank=True, max_length=500, null=True, upload_to=shop.models.image.thumb_dir, verbose_name='Photo (10%)')),
                ('image_thumb25', models.ImageField(blank=True, max_length=500, null=True, upload_to=shop.models.image.thumb_dir, verbose_name='Photo (25%)')),
                ('image_thumb50', models.ImageField(blank=True, max_length=500, null=True, upload_to=shop.models.image.thumb_dir, verbose_name='Photo (50%)')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
                'ordering': ['-created_at'],
            },
        ),
    ]
