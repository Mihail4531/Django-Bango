from django.contrib import admin
from django.utils.html import format_html # Библиотека для встроенной html-разметки
from .models import Category,  Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['-pk']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image_tag', 'category', 'is_active', 'is_banner', 'is_recent', 'is_featured', 'created_at']
    list_editable = ['category', 'is_active', 'is_banner', 'is_recent', 'is_featured']
    list_filter = ['category', 'is_active', 'is_banner', 'is_recent', 'is_featured']
    search_fields = ['title', 'slug', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ['title', 'slug']
    ordering = ['-created_at']

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius: 50%; object-fit: cover;" />'.format(obj.image.url))
        else:
            return None
    image_tag.short_description = 'Изображение'