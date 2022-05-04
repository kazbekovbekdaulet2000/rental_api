from rest_framework import serializers
from reaction.models.comment import Comment
from shop.serializers.category_serializer import RecursiveSerializer
from django.contrib.contenttypes.models import ContentType
from user.serializers.user_serializer import UserInfoSerializer


class CommentSerializer(serializers.ModelSerializer):
    owner = UserInfoSerializer(read_only=True)
    replies = RecursiveSerializer(
        source="comments_reply", many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'body', 'owner', 'reply',
                  'replies', 'created_at', 'updated_at', 'likes_count', 'bookmarks_count')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'body', 'reply')

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        lookup_field = self.context['view'].lookup_field
        validated_data['content_type'] = ContentType.objects.get_for_model(
            self.context['view'].model)
        validated_data['object_id'] = self.context['view'].kwargs[lookup_field]
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
