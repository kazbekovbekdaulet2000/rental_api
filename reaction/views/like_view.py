from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from reaction.models.like import Like
from reaction.serializers.like_serializer import LikeSerializer


class LikeAction(APIView):
    permission_classes = [permissions.IsAuthenticated]
    model = None
    lookup_field = None

    def post(self, request, *args, **kwargs):
        get_object_or_404(self.model, **{'id': self.kwargs[self.lookup_field]})
        serializer = LikeSerializer(data=request.data, context={
                                    'view': self, 'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
