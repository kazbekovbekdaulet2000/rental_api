from django.contrib import admin
from reaction.models.bookmark import Bookmark

from reaction.models.comment import Comment
from reaction.models.like import Like
from reaction.models.review import Review

class GenericAdmin(admin.ModelAdmin):
    list_fields = ('id', 'owner')
    readonly_fields = ('likes_count', 'comments_count', 'reviews_count', 'bookmarks_count')

# Register your models here.
admin.site.register(Comment, GenericAdmin)
admin.site.register(Like)
admin.site.register(Review, GenericAdmin)
admin.site.register(Bookmark)
