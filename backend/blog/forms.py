from django.contrib import admin
from .models import Category, Post

from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CategoryForm(forms.ModelForm):
    display_order = forms.IntegerField(initial=0, required=False)
    # updated = forms.DateTimeField(required=False, initial=datetime.datetime.now(), widget=forms.HiddenInput())

    class Meta:
        model = Category
        fields = [
            "title",
        ]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'author'
            'content',
            'category_name',
            'subcategory_name'
            'tags',
        ]


# Apply summernote to specific fields.
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea