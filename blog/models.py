from turtle import title
from django.db import models
from django.utils.translation import gettext_lazy as _
#from #django.utils.translation import ugettext_lazy as _

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=25,verbose_name=('Category title'))
    slug = models.SlugField(verbose_name="Slug",unique=True)
    image = models.ImageField(verbose_name="Add image",null=True,upload_to="categories_img")
    created_date = models.DateTimeField(verbose_name="created date",auto_now_add=True,null=True)
    updated_date = models.DateTimeField(verbose_name="updated date",auto_now=True,null=True)


    def __str__(self):
        return self.title
    




class News(models.Model):
    title= models.CharField(max_length=100,verbose_name=_("Name of News"))
    content= models.TextField(verbose_name=_("Main News"))
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True,verbose_name="Should be post?")
    image = models.ImageField(verbose_name="Add image",null=True,upload_to="news_image")
    slug= models.SlugField(verbose_name="Slug",null=True,unique=True)
    categories = models.ManyToManyField(Category,null=True,related_name='category_blog')
    clicked= models.IntegerField(editable=False,default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="News"
        verbose_name_plural="More News"
    

class Comment(models.Model):
    name = models.CharField(null=True,verbose_name="Name",max_length=30)
    created_date = models.DateTimeField(auto_now=True,verbose_name="Date")
    message = models.TextField(null=True,verbose_name="Comment")
    email = models.EmailField(null=True,verbose_name="Email")
    image = models.ImageField(null=True,verbose_name="Image",upload_to="Comment_User")
    news = models.ForeignKey(News,related_name="comment_news",verbose_name="News",on_delete=models.CASCADE)

    def __str__(self):
        return self.news.title

    class Meta:
        verbose_name="Comment"
        verbose_name_plural = "Comments"



# class Reply(models.Model):
#     name = models.CharField(null=True,verbose_name="Name",max_length=30)
#     created_date = models.DateTimeField(auto_now=True,verbose_name="Date")
#     message = models.TextField(null=True,verbose_name="Comment")
#     email = models.EmailField(null=True,verbose_name="Email")
#     image = models.ImageField(null=True,verbose_name="Image",upload_to="Comment_User")
#     news = models.ForeignKey(News,related_name="comment_news",verbose_name="News",on_delete=models.CASCADE)

#     def __str__(self):
#         return self.news.title

#     class Meta:
#         verbose_name="Reply"
#         verbose_name_plural = "Replies"




    

