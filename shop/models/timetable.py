from django.db import models
from django.dispatch import receiver
from config.common_models import AbstractModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from shop.models.product import Product
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
User = get_user_model()


class ProductTimeTableManager(models.Manager):
    def tables(self, product: Product):
        start_time = timezone.now() - timezone.timedelta(days=14)
        end_time = timezone.now() + timezone.timedelta(days=14)
        return self.get_queryset().filter(product=product, approved=True, start_time__gte=start_time, end_time__lte=end_time)


class ProductTimeTable(AbstractModel):
    product = models.ForeignKey(Product, related_name='rents', on_delete=models.CASCADE, null=False, blank=True)
    tenant = models.ForeignKey(User, verbose_name=_('арендатор'), on_delete=models.CASCADE, null=False, blank=True)
    total_price = models.FloatField(null=False, default=0.0)
    approved = models.BooleanField(default=False)

    times = ArrayField(models.PositiveIntegerField(blank=True, null=False), blank=True, null=True)

    objects = ProductTimeTableManager()

    def __str__(self):
        return 'Арендодатель:{}, Арендатор:{}'.format(self.product.owner, self.tenant)

    class Meta:
        ordering = ('-created_at',)

@receiver(models.signals.post_save, sender=ProductTimeTable)
def create_obj(sender, instance, **kwargs):
    if(instance.approved):
        timetable = instance.product.timetable.filter(id__in=list(instance.times))
        for time in timetable:
            time.tenant = instance.tenant
            time.save()