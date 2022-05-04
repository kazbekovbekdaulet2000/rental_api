from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import *
from django.contrib.auth.models import Group
from user.serializers.group_serializer import GroupSerializer


class GroupListView(generics.ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (permissions.AllowAny,)
