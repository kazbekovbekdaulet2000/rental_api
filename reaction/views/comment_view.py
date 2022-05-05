from rest_framework import generics
from rest_framework import permissions
from reaction.models.comment import Comment
from reaction.permissions import ObjectOwnerOrAdmin
from reaction.serializers.comment_serializer import CommentCreateSerializer, CommentSerializer


class CommentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    model = None
    lookup_field = 'id'

    def get_queryset(self):
        return Comment.objects\
            .get_object_by_model(model=self.model, id=self.kwargs.get(self.lookup_field))\
            .filter(reply__isnull=True)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CommentCreateSerializer
        return CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'comment_id'
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, ObjectOwnerOrAdmin]
    model = None

    def get_serializer_class(self):
        edit_methods = ("POST", "PUT", "PATCH", "DELETE")
        if self.request.method in edit_methods:
            return CommentCreateSerializer
        return CommentSerializer

    def get_queryset(self):
        return Comment.objects\
            .get_object_by_model(model=self.model, id=self.kwargs.get(self.lookup_field))
