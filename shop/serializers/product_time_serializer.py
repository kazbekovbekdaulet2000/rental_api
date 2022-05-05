from django.forms import ValidationError
from rest_framework import serializers
from shop.models.product import Product
from shop.models.product_time import ProductTime
from shop.models.timetable import ProductTimeTable
from shop.serializers.product_availability_serializer import ProductBaseAvailabilitySerializer
from shop.serializers.product_serializer import ProductBaseSerializer
from user.serializers.user_serializer import UserInfoSerializer


class ProductTimeTableSerializer(serializers.ModelSerializer):
    product = ProductBaseSerializer(many=False, read_only=True)
    tenant = UserInfoSerializer(many=False, read_only=True)
    times = serializers.SerializerMethodField()

    def get_times(self, obj):
        ids = obj.times
        data_list = []
        for data in ProductTime.objects.filter(id__in=ids).values():
            serializer = ProductBaseAvailabilitySerializer(data=data)
            if(serializer.is_valid(raise_exception=True)):
                data_list.append(serializer.data)
        return data_list

    class Meta:
        model = ProductTimeTable
        fields = ('product', 'id', 'tenant', 'total_price', 'times', 'approved')


class ProductTimeTableCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())
    times = serializers.ListField(
        child=serializers.IntegerField(), required=True)

    def validate(self, attrs):
        product = attrs['product']
        obj_times = ProductTime.objects.filter(product=product)

        if(ProductTimeTable.objects.filter(
                tenant=self.context['request'].user, product=product, times=attrs['times']).exists()):
            raise ValidationError('record already exists')

        for time in attrs['times']:
            if(not time in list(obj_times.values_list('id', flat=True))):
                raise ValidationError('time id is not true')
        for time in obj_times:
            if((time.id in attrs['times']) and (not time.tenant == None)):
                raise ValidationError(
                    f'{time.start_time}-{time.end_time} is not free for rent')
        return attrs

    def create(self, validated_data):
        product = validated_data['product']
        tenant = self.context['request'].user
        times = validated_data.pop('times')
        total_price = float(len(times) * product.price)
        try:
            instance = ProductTimeTable.objects.create(
                product=product, tenant=tenant, times=times, total_price=total_price)
        except TypeError:
            raise TypeError('error ocupied on creation of object')
        return instance
