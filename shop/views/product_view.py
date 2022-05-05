from rest_framework import generics
from rest_framework import permissions
from reaction.models.bookmark import Bookmark
from reaction.models.like import Like
from shop.models.image import ItemImage
from shop.models.product import Product
from shop.permissions import ProductOwnerAndLandlord, IsOwnerAndLandlord
from shop.serializers.product_image_serializer import ImageCreateSerializer, ImageSerializer
from shop.serializers.product_serializer import ProductBaseSerializer, ProductCreateSerializer
from rest_framework import parsers


class ProductList(generics.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerAndLandlord)
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return ProductCreateSerializer
        return ProductBaseSerializer


class ProductMyList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerAndLandlord, )

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return ProductCreateSerializer
        return ProductBaseSerializer


class ProductImageList(generics.ListCreateAPIView):
    parser_classes = (parsers.FormParser,
                      parsers.MultiPartParser, parsers.FileUploadParser)
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, ProductOwnerAndLandlord)
    pagination_class = None
    serializer_class = ImageCreateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return ItemImage.objects.filter(product=self.kwargs[self.lookup_field])

    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return ImageCreateSerializer
        return ImageSerializer


class ProductBookmarkedList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductBaseSerializer

    def get_queryset(self):
        ids = Bookmark.objects.get_user_objects(
            model=Product, user=self.request.user).values_list('object_id', flat=True)
        return Product.objects.filter(id__in=ids)


class ProductFavoriteList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductBaseSerializer

    def get_queryset(self):
        ids = Like.objects.get_user_objects(
            model=Product, user=self.request.user).values_list('object_id', flat=True)
        return Product.objects.filter(id__in=ids)


class ProductDetail(generics.RetrieveDestroyAPIView):
    lookup_field = 'id'
    permission_classes = (IsOwnerAndLandlord,)
    queryset = Product.objects.all()
    serializer_class = ProductBaseSerializer
