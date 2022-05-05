from rest_framework import serializers
from user.serializers.user_serializer import UserInfoSerializer


class ReactionGenericSerializer(serializers.ModelSerializer):
    owner = UserInfoSerializer(read_only=True)

    class Meta:
        fields = ('id', 'owner', 'created_at', 'updated_at', 'likes_count', 'bookmarks_count')
