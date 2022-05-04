from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
from config.common_models import AbstractModel, ContentTypeModel, ReactionsAbstract
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(AbstractModel, ContentTypeModel, ReactionsAbstract):
    body = models.TextField(blank=False)
    owner = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE, null=True)
    rating = models.PositiveIntegerField(null=False, default=5, validators=(MaxValueValidator(5), MinValueValidator(1)))

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
