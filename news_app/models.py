from django.utils import timezone
from django.db import models
from slugify import slugify


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100,null=True, blank=True)
    bio = models.TextField()
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    
class Category(models.Model):    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Tags(models.Model):
    tag = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.tag
    
    
    
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True, verbose_name='Published')
    slug = models.SlugField(max_length=200, unique=True, blank=True, default='')

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        permissions = [
            ('publish_news', 'Может публиковать новости'),
        ]
        
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) 
        super().save(*args, **kwargs)
    
    

    
    
