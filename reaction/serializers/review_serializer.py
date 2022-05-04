from rest_framework import serializers
from reaction.models.review import Review
from django.contrib.contenttypes.models import ContentType

from user.serializers.user_serializer import UserInfoSerializer


class ReviewSerializer(serializers.ModelSerializer):
    owner = UserInfoSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'rating', 'owner', 'created_at',
                  'updated_at', 'likes_count', 'bookmarks_count')


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'rating')

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        lookup_field = self.context['view'].lookup_field
        validated_data['content_type'] = ContentType.objects.get_for_model(
            self.context['view'].model)
        validated_data['object_id'] = self.context['view'].kwargs[lookup_field]
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
