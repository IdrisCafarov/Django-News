from django.contrib import admin
from blog.models import News,Category,Comment

# Register your models here.

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ['title','created_date','updated_date','draft','slug','clicked']
    exclude = ['title','content']

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['title','image','created_date','updated_date']


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['name','created_date','email']
