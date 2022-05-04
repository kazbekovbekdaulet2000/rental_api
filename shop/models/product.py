from django.db import models
from config.common_models import AbstractModel, ReactionsAbstract
from django.utils.translation import gettext_lazy as _
from shop.models.category import Category
from shop.models.tag import Tag
from user.models import User


class ProductManage(models.Manager):
    def list_related(self, product):
        category = product.category
        queryset = self.filter(category=category)
        queryset = self.get_related_products(queryset, category)
        return queryset.order_by('-likes_count', '-created_at')

    def get_related_products(self, queryset, category):
        if(category.parent == None or queryset.count() >= 10):
            return queryset
        else:
            queryset |= self.filter(category=category.parent)
            return self.get_related_products(queryset, category.parent)


CURRENCY_CHOICE = [
    ('T', 'Tenge'),
    ('EU', 'Euro'),
    ('USD', 'Dollar'),
]

RENT_TYPE = [
    ('hourly', 'for hours'),
    ('daily', 'for days'),
    ('weekly', 'for weeks'),
    ('monthly', 'for months'),
    ('yearly', 'for years'),
]


class Product(AbstractModel, ReactionsAbstract):
    name = models.CharField(max_length=255, null=False, blank=True)
    tags = models.ManyToManyField(Tag)
    description = models.CharField(max_length=4096, null=True, blank=True)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.DO_NOTHING, null=True, blank=True)
    owner = models.ForeignKey(
        User, related_name='products', on_delete=models.CASCADE, default=1)
    price = models.PositiveIntegerField(default=1000, null=False, blank=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICE, max_length=5, default='T', null=False, blank=True)
    active = models.BooleanField(default=True)
    rent_type = models.CharField(
        choices=RENT_TYPE, max_length=16, default='hourly', null=False, blank=True)

    objects = ProductManage()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
