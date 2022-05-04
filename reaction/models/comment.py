from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.db import models
from config.common_models import AbstractModel, ContentTypeModel, ReactionsAbstract
from shop.models.product import Product
from user.models import User
from django.db.models.signals import post_save, post_delete


class Comment(AbstractModel, ContentTypeModel, ReactionsAbstract):
    body = models.TextField(blank=False)
    owner = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE, null=True)
    reply = models.ForeignKey('self', related_name='comments_reply',
                              on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


@receiver(models.signals.post_save, sender=Comment)
def create_obj(sender, instance, **kwargs):
    obj = instance.content_object
    if(not obj.comments_count == None):
        obj.comments_count += 1
        obj.save()


@receiver(models.signals.post_delete, sender=Comment)
def delete_obj(sender, instance, **kwargs):
    obj = instance.content_object
    if(not obj.comments_count == None):
        obj.comments_count -= 1
        obj.save()
