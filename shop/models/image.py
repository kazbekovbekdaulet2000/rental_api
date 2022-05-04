import os
import sys
from turtle import width
from config.common_models import AbstractModel
from django.db import models
from shop.models.product import Product
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.translation import gettext_lazy as _
from PIL import Image
from io import BytesIO


def product_dir(instance, filename):
    return f"product/product_{instance.product.id}/{filename}"


def thumb_dir(instance, filename):
    return f"product/product_{instance.product.id}/thumbs/{filename}"


class ItemImage(AbstractModel):
    image = models.ImageField(verbose_name=_(
        'Photo'), null=False, blank=True, upload_to=product_dir)
    image_thumb240 = models.ImageField(verbose_name=_(
        'Photo (240px)'), upload_to=thumb_dir, max_length=500, null=True, blank=True)
    image_thumb480 = models.ImageField(verbose_name=_(
        'Photo (480px)'), upload_to=thumb_dir, max_length=500, null=True, blank=True)
    image_thumb720 = models.ImageField(verbose_name=_(
        'Photo (720px)'), upload_to=thumb_dir, max_length=500, null=True, blank=True)
    product = models.ForeignKey(
        Product, related_name='images', on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        return f"{self.product.name}"

    def create_thumbnail(self, newsize) -> InMemoryUploadedFile:
        if not self.image:
            return
        data_img = BytesIO()

        img = Image.open(self.image)
        img = img.convert('RGB')
        if(img.height/newsize <= 1 or img.width/newsize <= 1):
            return None

        if(img.width > img.height):
            width = int(newsize)
            height = int(img.height/(img.width/newsize))
        else:
            height = int(newsize)
            width = int(img.width/(img.height/newsize))

        THUMBNAIL_SIZE = (width, height)
        img.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
        img.save(data_img, format='jpeg', quality=100)

        return InMemoryUploadedFile(data_img,
                                    'ImageField',
                                    '%s_thumbnail_%spx.%s' % (os.path.splitext(
                                        self.image.name)[0], int(newsize), 'jpeg'),
                                    'jpeg',
                                    sys.getsizeof(data_img), None)

    def save(self, *args, **kwargs):
        if(not self.image_thumb240):
            self.image_thumb240 = self.create_thumbnail(240)
        if(not self.image_thumb480):
            self.image_thumb480 = self.create_thumbnail(480)
        if(not self.image_thumb720):
            self.image_thumb720 = self.create_thumbnail(720)

        force_update = False
        if self.id:
            force_update = True
        super(ItemImage, self).save(force_update=force_update, *args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
