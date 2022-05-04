from django.db import models
from config.common_models import AbstractModel
from django.utils.translation import gettext_lazy as _


class Category(AbstractModel):
    name = models.CharField(_('Name'), max_length=255, null=False, blank=True)
    parent = models.ForeignKey('self', verbose_name=_(
        'Parent category'), related_name='child', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
