
from django.contrib import admin
from .models import News, Category, Author, Tags

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tags)