from django.contrib import admin
from reaction.models.bookmark import Bookmark

from reaction.models.comment import Comment
from reaction.models.like import Like
from reaction.models.review import Review

# Register your models here.
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Review)
admin.site.register(Bookmark)
