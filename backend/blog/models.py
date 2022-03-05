from ast import Mod
from sre_constants import CATEGORY
from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    display_order = models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

CATEGORIES = (
    (0,"Language"),
    (1,"Travel"),
    (1,"Health")
)

class Category(Base):
    category_no = models.IntegerField(choices=CATEGORIES, default=0)


class SubCategory(Category):
    sub_category = models.CharField(max_length=10, blank=False)

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(SubCategory):
    # post_name = models.ForeignKey(Category, on_delete= models.CASCADE,related_name='category_name')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')  
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
