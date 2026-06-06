from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import News, Category
from .forms import RegistrationForm, User_Update_Form, Profile_Update_Form
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages


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

def search_autocomplete(request):
    q = request.GET.get('q', '').strip()
    if len(q) < 2:
        return JsonResponse({'results': []})

    results = (
        News.objects
        .filter(
            Q(title__icontains=q) |
            Q(category__name__icontains=q) |
            Q(tags__tag__icontains=q) |
            Q(author__name__icontains=q) |
            Q(content__icontains=q)
        )
        .filter(is_published=True)
        .distinct()
        .order_by('-created_at')
        .values('slug', 'title', 'category__name')[:8]
    )

    data = [
        {
            'id': n['slug'],
            'title': n['title'],
            'category': n['category__name'] or '',
            'url': f"/product/{n['slug']}/"
        }
        for n in results
    ]

    return JsonResponse({'results': data, 'total': len(data)})



def category_news(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    items = News.objects.filter(category=category).order_by('-created_at')
    categories = Category.objects.all()
    
    paginator = Paginator(items, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'home.html', {'news': page_obj, 'categories': categories, 'selected_category': category, 'page_obj': page_obj})


def product_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    categories = Category.objects.all()
    return render(request, 'product_detail.html', {'news': news, 'categories': categories})


@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = User_Update_Form(request.POST, instance=request.user)
        p_form = Profile_Update_Form(request.POST, request.FILES, instance=request.user.user_profile)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, 'Ваш профиль успешно обновлен!')
        return redirect('profile')
    else:
        u_form = User_Update_Form(instance=request.user)
        p_form = Profile_Update_Form(instance=request.user.user_profile)
    return render(request, 'profile.html', {'u_form': u_form, 'p_form': p_form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


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