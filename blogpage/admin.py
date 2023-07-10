from django.contrib import admin
from blogpage.models import BlogPostTable


@admin.register(BlogPostTable)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
