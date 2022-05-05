from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from shop.models.product_time import ProductTime
from shop.models.timetable import ProductTimeTable
from shop.permissions import RentRequestParticipantsOrAdmin
from shop.serializers.product_time_serializer import ProductTimeTableSerializer
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group


class ProductRentView(generics.RetrieveAPIView, mixins.DestroyModelMixin):
    lookup_field = 'id'
    lookup_url_kwarg = 'request_id'
    queryset = ProductTimeTable.objects.all()
    permission_classes = (permissions.IsAuthenticated,
                          RentRequestParticipantsOrAdmin)
    serializer_class = ProductTimeTableSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(["POST"])
def confirm(request, *args, **kwargs):
    if(request.user.is_anonymous):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if(not Group.objects.get(name='landlord') in request.user.groups.all()):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if(not kwargs['id'] in list(request.user.products.all().values_list('id', flat=True))):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    rent_request = get_object_or_404(ProductTimeTable, **{'id': kwargs['request_id']})
    times = ProductTime.objects.filter(id__in = list(rent_request.times))
    for time in times:
        if(time.tenant == None):
            time.tenant = rent_request.tenant
            time.save()
        else:
            return Response({'error': 'at this time product is unavailable'},status=status.HTTP_400_BAD_REQUEST)
    rent_request.approved = True
    rent_request.save()

    return Response(status=status.HTTP_202_ACCEPTED)
