from django.contrib import admin
from .models import Blog, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'status',
        'is_featured',
        'views',
        'created_at',
    )

    list_filter = (
        'status',
        'is_featured',
        'category',
        'created_at',
    )

    search_fields = (
        'title',
        'content',
        'short_description',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    readonly_fields = (
        'views',
        'created_at',
        'updated_at',
    )

    ordering = ('-created_at',)