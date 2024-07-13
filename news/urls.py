from django.urls import path

from news.views import news_get

urlpatterns = [
    path(r"<slug:slug>", news_get),
]
