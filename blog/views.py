
from blog.models import News,Category,Comment
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import F
from blog.forms import CommentForm
# Import Pagiantor
from django.core.paginator import Paginator


# Create your views here.


def news_view(request):
    news=News.objects.filter(draft=True)
    populars= news.order_by('-clicked')
    latests = news.order_by('-updated_date')
    
    context={
        "news":news,
        "populars":populars,
        "latests":latests,
        
    }

    return render(request,"main/index.html",context)

    



def details_view(request,slug):
    context={}
    post = get_object_or_404(News,slug=slug)
    news=News.objects.filter(draft=True)
    populars= news.order_by('-clicked').exclude(pk = post.id)
    context['populars'] = populars
    post.clicked = F('clicked')+1
    post.save(update_fields=['clicked'])
    if request.method == "POST":
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.news = post                 
            comment.image = request.FILES['image']
            comment.save()
            return redirect('blog:details',slug=post.slug)
    else:
        form = CommentForm()
        context['form'] = form

    comments = Comment.objects.filter(news=post)
    context['comments'] = comments.order_by('-id')
    context['objects']=post

    return render(request,'details/single.html',context)


def category_views(request,slug):
    category = get_object_or_404(Category,slug=slug)
    blog = category.category_blog.all()
    news= blog.filter(draft=True)


    #Paginator
    p = Paginator(news,14)
    page = request.GET.get('page')
    venues = p.get_page(page)
    

    
    populars= news.order_by('-clicked')
    
    context = {
        "news":news,
        "venues":venues,
        "category":category,
        "populars":populars,
        
    }   

    return render(request,'category/category.html',context)


def categories_view(request):
    news=News.objects.filter(draft=True)
    populars= news.order_by('-clicked')
    context={}
    context['populars']=populars
    
    


    

    return render(request,"categories/categories.html",context)

def contact_view(request):
    context={}
    

    news=News.objects.filter(draft=True)
    populars= news.order_by('-clicked')
    context['populars'] = populars
   
    
    return render(request,"contact/contact.html",context)


def search_view(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched_news = News.objects.filter(title__contains=searched)
        
        news=News.objects.filter(draft=True)
        populars= news.order_by('-clicked')

        

        context = {
            "searched_news":searched_news,
            "searched":searched,
            "populars":populars
        }
        return render(request,"searched_news/searched_news.html",context)



def all_news_view(request):
    news = News.objects.filter(draft=True)
    populars = news.order_by('-clicked')
    p = Paginator(news,14)
    page = request.GET.get('page')
    venues = p.get_page(page)
    
    
    context = {
        "all_news":news,
        "populars":populars,
        "venues":venues
    }

    return render(request,"all_news/all_news.html",context)
