from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'surname', 'created_at', 'is_staff']
    ordering = ['-created_at']
    readonly_fields = ('email', 'name', 'surname', 'birth_date',
                       'image', 'city', 'description', 'user_type')
    list_filter = ['is_staff', 'verified']
    search_fields = ['email', 'name', 'surname']


admin.site.register(User)
