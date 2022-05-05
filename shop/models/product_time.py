from django.db import models
from config.common_models import AbstractModel
from django.utils.translation import gettext_lazy as _
from shop.models.product import Product
import datetime
from shop.models.timetable import User
from django.utils import timezone


class ProductTimeManager(models.Manager):
    def isExist(self, product_id, start_time, end_time):
        change = end_time - start_time - datetime.timedelta(minutes=1)
        return self.get_queryset().filter(product_id=product_id, start_time__gte=(start_time - change), end_time__lte=(end_time+change)).exists()

    def isFree(self, product_id):
        date = timezone.now()
        
        return self.get_queryset().filter(product_id=product_id, start_time__gte=date, end_time__lte=date).exists()

class ProductTime(AbstractModel):
    product = models.ForeignKey(Product, related_name='timetable', on_delete=models.CASCADE, null=False, blank=True)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    objects = ProductTimeManager()

    def __str__(self):
        return f"{self.product.name} ({self.start_time}-{self.end_time})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product Availability'
        verbose_name_plural = 'Products Availability'
