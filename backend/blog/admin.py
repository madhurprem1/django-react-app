from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin

# Register your models here.
from .models import  Category, SubCategory, Post


class AddCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class AddSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'category_name', 'subcategory_name',)
    list_filter = ("title",)
    search_fields = ['title', 'content',]
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Category, AddCategoryAdmin)
admin.site.register(SubCategory, AddSubCategoryAdmin)
admin.site.register(Post, PostAdmin)