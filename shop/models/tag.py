from django.db import models
from config.common_models import AbstractModel
from django.utils.translation import gettext_lazy as _


class Tag(AbstractModel):
    tag = models.CharField(_('tag'), max_length=255, null=False, blank=True)
    description = models.CharField(
        _('description'), max_length=4096, null=False, blank=True)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
