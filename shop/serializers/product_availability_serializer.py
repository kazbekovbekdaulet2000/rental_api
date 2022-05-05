from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from shop.models.product import Product
from shop.models.product_time import ProductTime
import datetime


class ProductBaseAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTime
        fields = ('id', 'start_time', 'end_time')


class ProductAvailabilitySerializer(ProductBaseAvailabilitySerializer):
    available = serializers.SerializerMethodField()

    def get_available(self, obj: ProductTime):
        return obj.tenant == None

    class Meta:
        model = ProductTime
        fields = ('id', 'start_time', 'end_time', 'available')


class ProductAvailabilityCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    start_time = serializers.DateTimeField(required=True)
    end_time = serializers.DateTimeField(read_only=True)

    def validate(self, attrs):
        start_time = attrs['start_time']
        product_id = self.context['view'].kwargs['id']
        product = get_object_or_404(Product, **{'id': product_id})

        if(product.rent_type == 'hourly'):
            end_time = start_time + datetime.timedelta(hours=1)
        if(product.rent_type == 'daily'):
            end_time = start_time + datetime.timedelta(days=1)
        if(product.rent_type == 'weekly'):
            end_time = start_time + datetime.timedelta(weeks=1)
        if(product.rent_type == 'monthly'):
            end_time = start_time + datetime.timedelta(days=30)
        if(product.rent_type == 'yearly'):
            end_time = start_time + datetime.timedelta(days=365)

        attrs['end_time'] = end_time
        if(ProductTime.objects.isExist(product_id, start_time, end_time)):
            raise ValidationError('already exist')
        return attrs

    def create(self, validated_data):
        start_time = validated_data['start_time']
        end_time = validated_data['end_time']
        product_id = self.context['view'].kwargs['id']
        try:
            if(not ProductTime.objects.isExist(product_id, start_time, end_time)):
                instance = ProductTime.objects.create(
                    product_id=product_id, start_time=start_time, end_time=end_time)
            else:
                return 'time exists '
        except TypeError:
            raise TypeError('error ocupied on creation of object')
        return instance
