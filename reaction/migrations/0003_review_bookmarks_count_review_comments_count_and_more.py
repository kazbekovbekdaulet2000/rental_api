# Generated by Django 4.0.4 on 2022-05-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reaction', '0002_comment_bookmarks_count_comment_comments_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='bookmarks_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='comments_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
