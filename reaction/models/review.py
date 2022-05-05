from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.db import models
from config.common_models import AbstractModel, ContentTypeModel, ReactionsAbstract
from shop.models.product import Product
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(AbstractModel, ContentTypeModel, ReactionsAbstract):
    body = models.TextField(blank=False)
    owner = models.ForeignKey(
        User, related_name='review', on_delete=models.CASCADE, null=True)
    rating = models.PositiveIntegerField(null=False, default=5, validators=(
        MaxValueValidator(5), MinValueValidator(1)))

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


@receiver(models.signals.post_save, sender=Review)
def create_obj(sender, instance, **kwargs):
    obj = instance.content_object
    if(type(obj) == Product and kwargs['created']):
        user = obj.owner
        user.rating = (user.rating + instance.rating)/2
        user.save()
    try:
        if(not obj.reviews_count == None):
            obj.reviews_count += 1
            obj.save()
    except: pass


@receiver(models.signals.post_delete, sender=Review)
def delete_obj(sender, instance, **kwargs):
    obj = instance.content_object
    try:
        if(not obj.reviews_count == None):
            obj.reviews_count -= 1
            obj.save()
    except: pass
