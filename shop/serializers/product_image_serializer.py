from itertools import product
from rest_framework import serializers
from shop.models.image import ItemImage
from shop.models.product import Product


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ('id', 'image', 'image_thumb240',
                  'image_thumb480', 'image_thumb720')


class ImageCreateSerializer(serializers.Serializer):
    image = serializers.ImageField(label='Photo', max_length=100, read_only=False)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    def create(self, validated_data):
        return ItemImage.objects.create(**validated_data)