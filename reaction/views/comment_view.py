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
    permission_classes = [ObjectOwnerOrAdmin,permissions.IsAuthenticatedOrReadOnly]
    model = None

    def get_serializer_class(self):
        edit_methods = ("POST", "PUT", "PATCH", "DELETE")
        if self.request.method in edit_methods:
            return CommentCreateSerializer
        return CommentSerializer

    def get_queryset(self):
        return Comment.objects\
            .get_object_by_model(model=self.model, id=self.kwargs.get(self.lookup_field))\


# class CommentLike(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     model = None

#     def post(self, request, *args, **kwargs):
#         item = Comment.objects.get(id=self.kwargs['comment_id'])
#         if(request.user in item.likes.all()):
#             item.likes.remove(request.user)
#             return Response({"liked": False}, status=status.HTTP_202_ACCEPTED)
#         else:
#             item.likes.add(request.user)
#             return Response({"liked": True}, status=status.HTTP_202_ACCEPTED)
