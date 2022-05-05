from rest_framework import serializers
from shop.models.product import Product
from shop.serializers.product_image_serializer import ImageSerializer
from shop.serializers.tag_serializer import TagSerializer
from user.serializers.user_serializer import UserInfoSerializer


class ProductBaseSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True)
    available = serializers.SerializerMethodField()
    owner = UserInfoSerializer(read_only=True)

    def get_available(self, obj: Product) -> bool:
        return obj.timetable.isFree(obj.id)

    class Meta:
        model = Product
        fields = ('id', 'name', 'tags', 'description',
                  'category', 'images', 'created_at',
                  'likes_count', 'comments_count', 'bookmarks_count', 'reviews_count',
                  'active', 'price', 'currency', 'available', 'owner', 'rent_type')


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description',
                  'category', 'active', 'price',
                  'currency', 'rent_type')

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
