from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import News, Category
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password != password_confirm:
            return render(request, 'register.html', {'error': 'Пароли не совпадают'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Пользователь уже существует'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('home')
    
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Неверные учётные данные'})
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')