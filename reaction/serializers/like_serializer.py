from rest_framework import serializers
from reaction.models.like import Like
from django.contrib.contenttypes.models import ContentType


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'object_id')

    def create(self, validated_data):
        lookup_field = self.context['view'].lookup_field

        obj = Like.objects.get_object_by_user(
            self.context['view'].model,
            self.context['view'].kwargs[lookup_field],
            self.context['request'].user
        )
        if(obj.count() >= 1):
            obj.delete()
            return validated_data
        else:
            validated_data['content_type'] = ContentType.objects.get_for_model(
                self.context['view'].model)
            validated_data['object_id'] = self.context['view'].kwargs[lookup_field]
            validated_data['owner'] = self.context['request'].user
            return super().create(validated_data)
