from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, Category

def home(request):
    items = News.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'home.html', {'news': items, 'categories': categories})


def category_news(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    items = News.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'news': items, 'categories': categories, 'selected_category': category})


def product_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'product_detail.html', {'news': news})