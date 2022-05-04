from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.db import models
from config.common_models import AbstractModel, ContentTypeModel
from user.models import User
from django.db.models.signals import post_save, post_delete


class Bookmark(AbstractModel, ContentTypeModel):
    owner = models.ForeignKey(
        User, related_name='bookmarks', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'


@receiver(models.signals.post_save, sender=Bookmark)
def create_obj(sender, instance, **kwargs):
    obj = instance.content_object
    try:
        obj.bookmarks_count += 1
        obj.save()
    except AttributeError:
        pass


@receiver(models.signals.post_delete, sender=Bookmark)
def delete_obj(sender, instance, **kwargs):
    obj = instance.content_object
    try:
        obj.bookmarks_count -= 1
        obj.save()
    except AttributeError:
        pass
