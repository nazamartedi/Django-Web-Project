from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    # indicates the name of the object in the db
    class Meta():
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
        def __str__(self):
            return self.name
        

class Post(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    # indicates the name of the object in the db
    class Meta():
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        
        def __str__(self):
            return self.title
