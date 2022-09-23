from blog.models import *
from datetime import datetime

def extras(request):
    context={}
    categories = Category.objects.all()
    date_now= datetime.now()
    context['categories']=categories
    context['date_now'] = date_now
    
    return context