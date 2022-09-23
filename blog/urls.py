from django.urls import path
from blog.views import news_view,details_view,category_views,categories_view,contact_view,search_view,all_news_view


app_name="blog"

urlpatterns = [
    path('',news_view,name="index"),
    path('details/<slug>/',details_view,name="details"),
    path('category/<slug>/',category_views,name='category'),
    path('categories',categories_view,name="category_main"),
    path('contact',contact_view,name="contact"),
    path('search_venues',search_view,name="search_venues"),
    path('all_news',all_news_view,name='all_news')
    
    
]
