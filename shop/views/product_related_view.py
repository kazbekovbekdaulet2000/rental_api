from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from shop.models.product import Product
from shop.serializers.product_serializer import ProductBaseSerializer


class ProductRelatedList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    serializer_class = ProductBaseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        product = get_object_or_404(Product, **{'id': self.kwargs[self.lookup_field]})
        return Product.objects.list_related(product)
