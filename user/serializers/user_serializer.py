from email.policy import default
from django.contrib.auth import get_user_model
from rest_framework import serializers
from datetime import date
from django.contrib.auth.models import Group

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    user_type = serializers.ChoiceField(
        choices=('landlord', 'tenant'), default='tenant', write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'surname',
                  'birth_date', 'password', 're_password', 'user_type']
        extra_fields = {
            'password': {'write_only': True},
            're_password': {'write_only': True},
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
        user_type = validated_data.pop('user_type')
        group = Group.objects.get(name=user_type)
        user = User.objects.create(**validated_data)
        user.groups.add(group)
        return user

    def save(self):
        del self.validated_data['re_password']
        user_type = self.validated_data.pop('user_type')
        group = Group.objects.get(name=user_type)
        account = User(
            **self.validated_data
        )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        account.groups.add(group)


class UserInfoSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    def get_user_type(self, user: User):
        if Group.objects.get(name='landlord') in user.groups.all():
            return Group.objects.get(name='landlord').name
        return Group.objects.get(name='tenant').name

    class Meta:
        model = User
        fields = ['id', 'email', 'image', 'name',
                  'surname', 'birth_date', 'description', 'rating',
                  'verified', 'is_superuser', 'user_type']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'surname', 'description',
                  'image', 'birth_date', 'groups']
        read_only_fields = ['id', 'email']
