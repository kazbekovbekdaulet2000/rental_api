from django.urls import path
from reaction.models.comment import Comment
from reaction.models.review import Review
from reaction.views.bookmark_view import BookmarkAction
from reaction.views.comment_view import CommentDetail, CommentList
from reaction.views.like_view import LikeAction
from reaction.views.review_view import ReviewDetail, ReviewList
from shop.models.product import Product
from shop.views.category_view import CategoryList
from shop.views.product_availability_view import ProductAvailabilityList
from shop.views.product_related_view import ProductRelatedList
from shop.views.product_view import ProductBookmarkedList, ProductDetail, ProductFavoriteList, ProductImageList, ProductList
from shop.views.timetable_view import ProductTimeTableList


urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('products/', ProductList.as_view()),
    path('products/bookmarked/', ProductBookmarkedList.as_view()),
    path('products/favorite/', ProductFavoriteList.as_view()),
    path('products/<int:id>/', ProductDetail.as_view()),

    path('products/<int:id>/related/', ProductRelatedList.as_view()),
    path('products/<int:id>/timetable/', ProductAvailabilityList.as_view()),
    path('products/<int:id>/images/', ProductImageList.as_view()),

    # product reactions
    path('products/<int:id>/like/',
         LikeAction.as_view(model=Product, lookup_field='id')),
    path('products/<int:id>/save/',
         BookmarkAction.as_view(model=Product, lookup_field='id')),

    #  product comments && comment reactions
    path('products/<int:id>/comments/', CommentList.as_view(model=Product)),
    path('products/<int:id>/comments/<int:comment_id>/',
         CommentDetail.as_view(model=Product)),
    path('products/<int:id>/comments/<int:comment_id>/like/',
         LikeAction.as_view(model=Comment, lookup_field='comment_id')),
    path('products/<int:id>/comments/<int:comment_id>/save/',
         BookmarkAction.as_view(model=Comment, lookup_field='comment_id')),

    #  product reviews && review reactions
    path('products/<int:id>/reviews/', ReviewList.as_view(model=Product)),
    path('products/<int:id>/reviews/<int:review_id>/',
         ReviewDetail.as_view(model=Product)),
    path('products/<int:id>/reviews/<int:review_id>/like/',
         LikeAction.as_view(model=Review, lookup_field='review_id')),
    path('products/<int:id>/reviews/<int:review_id>/save/',
         BookmarkAction.as_view(model=Review, lookup_field='review_id')),


    path('products/<int:id>/requests/', ProductTimeTableList.as_view()),

    # rent TODO
    path('products/<int:id>/requests/<int:request_id>/',
         ProductTimeTableList.as_view()),
    path('products/<int:id>/requests/<int:request_id>/confirm/',
         ProductTimeTableList.as_view()),
]
