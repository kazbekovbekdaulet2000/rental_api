from rest_framework import generics
from rest_framework import permissions
from shop.models.timetable import ProductTimeTable
from shop.serializers.product_time_serializer import ProductTimeTableSerializer, ProductTimeTableCreateSerializer
from django.contrib.auth.models import Group


class ProductTimeTableList(generics.ListCreateAPIView):
    queryset = ProductTimeTable.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        if(Group.objects.get(name='landlord') in self.request.user.groups.all()):
            return ProductTimeTable.objects.filter(product__id=self.kwargs['id'], product__owner=self.request.user)
        return ProductTimeTable.objects.filter(product__id=self.kwargs['id'], tenant=self.request.user)

    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return ProductTimeTableCreateSerializer
        return ProductTimeTableSerializer
