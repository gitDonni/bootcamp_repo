from django.shortcuts import render
from .models import News



def home(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})


def news_detail(request, id):
    news = News.objects.get(id=id)
    return render(request, 'news_detail.html', {'news': news})

