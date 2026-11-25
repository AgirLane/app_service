from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    list_display = ('title', 'created_at', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'text')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass