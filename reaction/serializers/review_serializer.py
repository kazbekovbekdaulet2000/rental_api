from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reaction.models.review import Review
from django.contrib.contenttypes.models import ContentType
from reaction.serializers.generic_serializer import ReactionGenericSerializer


class ReviewSerializer(ReactionGenericSerializer):
    class Meta:
        model = Review
        fields = ReactionGenericSerializer.Meta.fields + ('rating', 'owner')


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'rating')

    def validate(self, attrs):
        id = self.context['view'].kwargs[self.context['view'].lookup_field]
        user = self.context['request'].user
        if(Review.objects.get_object_by_user(self.context['view'].model, id, user).exists() and self.context['request'].method == "POST"):
            raise ValidationError('already exists')
        return super().validate(attrs)

    def create(self, validated_data):
        lookup_field = self.context['view'].lookup_field
        validated_data['content_type'] = ContentType.objects.get_for_model(
            self.context['view'].model)
        validated_data['object_id'] = self.context['view'].kwargs[lookup_field]
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
