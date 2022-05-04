# Generated by Django 4.0.4 on 2022-05-04 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0019_producttimetable_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttime',
            name='tentor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='producttime',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='timetable', to='shop.product'),
        ),
    ]
