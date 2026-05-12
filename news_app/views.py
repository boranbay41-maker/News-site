from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, Category

def home(request):
    items = News.objects.all()
    return render(request, 'home.html', {'news': items})


def product_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'product_detail.html', {'news': news})



def product_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'product_detail.html', {'news': news})