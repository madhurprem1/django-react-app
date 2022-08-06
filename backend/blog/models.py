from ast import Mod
from sre_constants import CATEGORY
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Base(models.Model):
    display_order = models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)


class Category(Base):
    title = models.CharField(max_length=20, blank=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class SubCategory(Base):
    name = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(Base):
    # post_name = models.ForeignKey(Category, on_delete= models.CASCADE,related_name='category_name')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')  
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category')
    subcategory_name = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='SubCategory')
    delete_flag = models.BooleanField(default=True, blank=False)
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    tags = TaggableManager()

    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()

