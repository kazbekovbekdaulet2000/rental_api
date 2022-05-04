from django.contrib import admin
from shop.models.category import Category
from shop.models.product import Product
from shop.models.product_time import ProductTime
from shop.models.tag import Tag
from shop.models.timetable import ProductTimeTable
from shop.models.image import ItemImage


class ProductImageAdmin(admin.TabularInline):
    exclude = ('image_thumb240', 'image_thumb480', 'image_thumb720')
    model = ItemImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('likes_count', 'comments_count', 'bookmarks_count')
    search_fields = ('name', 'description')
    inlines = [ProductImageAdmin]


admin.site.register([Category, Tag, ProductTimeTable, ProductTime])
admin.site.register(Product, ProductAdmin)
