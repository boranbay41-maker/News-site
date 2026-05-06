from django.utils import timezone
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField()
    
    def __str__(self):
        return self.name

    
class Category(models.Model):    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Tags(models.Model):
    tag = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tag
    
    
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.title
    

    
    
