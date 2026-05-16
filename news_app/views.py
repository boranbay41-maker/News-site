from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, Category
from django.db.models import Q

def home(request):
    poisk = request.GET.get('q')
    if poisk:
        items = News.objects.filter(
            Q(title__icontains=poisk) | 
            Q(content__icontains=poisk) |
            Q(category__name__icontains=poisk) |
            Q(tags__tag__icontains=poisk) |
            Q(author__name__icontains=poisk)
        ).distinct().order_by('-created_at')
    else:
        items = News.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    
    paginator = Paginator(items, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'home.html', {'news': page_obj, 'categories': categories, 'page_obj': page_obj})


def category_news(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    items = News.objects.filter(category=category).order_by('-created_at')
    categories = Category.objects.all()
    
    paginator = Paginator(items, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'home.html', {'news': page_obj, 'categories': categories, 'selected_category': category, 'page_obj': page_obj})


def product_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'product_detail.html', {'news': news})