from rest_framework import serializers
from shop.models.category import Category


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(
            instance, context=self.context)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    child_categories = RecursiveSerializer(
        source="child", many=True, read_only=True)
    products_count = serializers.SerializerMethodField(read_only=True)

    def get_products_count(self, obj) -> int:
        def recursive_count(category: Category) -> int:
            count = 0
            for child in category.child.all():
                count += recursive_count(child)
            return category.products.count() + count
        return recursive_count(obj)

    class Meta:
        model = Category
        fields = ('id', 'child_categories', 'name', 'products_count')
