from django.shortcuts import render

from news.models import News


def news_get(request, slug):
    news = News.objects.get(slug=slug)
    context = {
        "news": news,
    }
    return render(request, "news/news.html", context)
