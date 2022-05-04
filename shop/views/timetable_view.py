from rest_framework import generics
from rest_framework import permissions
from shop.models.timetable import ProductTimeTable
from shop.serializers.product_time_serializer import ProductTimeTableSerializer, ProductTimeTableCreateSerializer


class ProductTimeTableList(generics.ListCreateAPIView):
    queryset = ProductTimeTable.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def get_serializer_class(self):
        if(self.request.method=="POST"):
            return ProductTimeTableCreateSerializer
        return ProductTimeTableSerializer
