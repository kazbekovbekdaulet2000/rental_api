from rest_framework import permissions
from shop.models.product_time import ProductTime
from shop.permissions import ProductOwnerAndLandlord
from rest_framework import generics
from shop.serializers.product_availability_serializer import ProductAvailabilityCreateSerializer, ProductAvailabilitySerializer


class ProductAvailabilityList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ProductOwnerAndLandlord]
    queryset = ProductTime.objects.all()

    def get_serializer_class(self):
        if(self.request.method =="POST"):
            return ProductAvailabilityCreateSerializer
        return ProductAvailabilitySerializer