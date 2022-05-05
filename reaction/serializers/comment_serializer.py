from django.forms import ValidationError
from rest_framework import serializers
from reaction.bad_words import BAD_WORDS
from reaction.models.comment import Comment
from reaction.serializers.generic_serializer import ReactionGenericSerializer
from shop.serializers.category_serializer import RecursiveSerializer
from django.contrib.contenttypes.models import ContentType
import re


class CommentSerializer(ReactionGenericSerializer):
    replies = RecursiveSerializer(
        source="comments_reply", many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ReactionGenericSerializer.Meta.fields + \
            ('body', 'reply', 'replies')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'body', 'reply')

    def validate_body(self, text):
        words = set(re.sub("[^\w]", " ",  text).split())
        if any(censored_word in words for censored_word in BAD_WORDS):
            raise ValidationError("censored content!")
        return text

    def create(self, validated_data):
        lookup_field = self.context['view'].lookup_field
        validated_data['content_type'] = ContentType.objects.get_for_model(
            self.context['view'].model)
        validated_data['object_id'] = self.context['view'].kwargs[lookup_field]
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
