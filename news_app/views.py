from django.shortcuts import render
from .models import News

# Create your views here.

def home(request):
    items = News.objects.all()
    return render(request, 'home.html', {'news': items})