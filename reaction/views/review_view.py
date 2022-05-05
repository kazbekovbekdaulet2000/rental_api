from rest_framework import generics
from rest_framework import permissions
from reaction.models.review import Review
from reaction.permissions import ObjectOwnerOrAdmin
from reaction.serializers.review_serializer import ReviewCreateSerializer, ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    model = None
    lookup_field = 'id'

    def get_queryset(self):
        return Review.objects\
            .get_object_by_model(model=self.model, id=self.kwargs.get(self.lookup_field))

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ReviewCreateSerializer
        return ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'review_id'
    permission_classes = [ObjectOwnerOrAdmin,
                          permissions.IsAuthenticatedOrReadOnly]
    model = None

    def get_serializer_class(self):
        edit_methods = ("POST", "PUT", "PATCH", "DELETE")
        if self.request.method in edit_methods:
            return ReviewCreateSerializer
        return ReviewSerializer

    def get_queryset(self):
        return Review.objects\
            .get_object_by_model(model=self.model, id=self.kwargs.get(self.lookup_field))
