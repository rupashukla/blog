from django.contrib import admin
from .models import Blog, User,Like
# Register your models here.

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ['blogid', 'blogtitle', 'description', 'Content', 'creationdata']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['blogid','blogtitle','description','Content']

admin.site.register(User)
admin.site.register(Like)