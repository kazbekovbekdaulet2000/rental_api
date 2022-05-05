from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from reaction.views.like_view import LikeAction
from reaction.views.review_view import ReviewDetail, ReviewList
from shop.models.timetable import User
from user.views.groups_view import GroupListView
from user.views.logout_view import logout
from user.views.user_views import ResetPassword, UserCreateView, UserView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('signup/', UserCreateView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('reset/', ResetPassword.as_view(type="reset")),
    path('reset/confirm/', ResetPassword.as_view(type="confirm")),
    path('reset/force/', ResetPassword.as_view(type="force")),
    path('profile/', UserView.as_view()),
    path('groups/', GroupListView.as_view()),
    path('logout/', logout, name='logout'),
    path('profile/<int:id>/reviews/',
         ReviewList.as_view(model=User)),
]
