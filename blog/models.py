from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField( max_length=50)
    image = models.ImageField(upload_to='post/')
    #tags = ''
    publish_date = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User, related_name='Post_author', on_delete=models.CASCADE)
    content = models.CharField(max_length=2500)
    category = models.ForeignKey('Category', related_name='Post_category',on_delete=models.CASCADE)
    
    
    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Category(models.Model):
    title = models.TextField(max_length=50)
    
    
    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'