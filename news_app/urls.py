from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_news, name='category_news'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]