from django.contrib import admin
from .models import News, Category, Author, Tags

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tags)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at', 'is_published')
    list_filter = ('category', 'author', 'tags', 'is_published')
    search_fields = ('title', 'content')
    filter_horizontal = ('tags',)
    date_hierarchy = 'created_at'
