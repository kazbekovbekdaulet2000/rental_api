from rest_framework import generics
from rest_framework import permissions
from shop.models.category import Category
from shop.serializers.category_serializer import CategorySerializer


class CategoryList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Category.objects.filter(child__isnull=False)\
        # .annotate(items_count=Count('products')).filter(items_count__gte=0)
    serializer_class = CategorySerializer
