from django.contrib.auth import get_user_model
from rest_framework import serializers
from datetime import date

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'surname',
                  'birth_date', 'password', 're_password', 'groups']
        extra_fields = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs['password']
        re_password = attrs['re_password']

        if password != re_password:
            raise serializers.ValidationError(
                {'password': 'Password must match'})
        min_date = date(1945, 1, 1)
        max_date = date(2017, 1, 1)
        if(attrs['birth_date'] < min_date or attrs['birth_date'] > max_date):
            raise serializers.ValidationError(
                {'birth_date': 'not match'})
        return attrs

    def create(self, validated_data):
        groups_data = validated_data.pop('groups')
        user = User.objects.create(**validated_data)
        for group_data in groups_data:
            user.groups.add(group_data)
        return user

    def save(self):
        del self.validated_data['re_password']
        groups_data = self.validated_data.pop('groups')
        user = User.objects.create(**self.validated_data)
        for group_data in groups_data:
            user.groups.add(group_data)
        # groups_data = self.validated_data.pop('groups')
        # account = User(
        #     **self.validated_data
        # )
        # password = self.validated_data['password']
        # account.set_password(password)
        # account.save()
        # for group_data in groups_data:
        #     account.groups.add(group_data)


class UserInfoSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'image', 'name',
                  'surname', 'birth_date', 'description', 'verified', 'is_superuser', 'groups']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'surname', 'description',
                  'image', 'birth_date', 'groups']
        read_only_fields = ['id', 'email']
