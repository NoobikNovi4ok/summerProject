from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="home"),
    path("catalog", views.catalog, name="catalog"),
    path("search", views.catalog, name="search"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    # path("job", views.job, name="job"),
]
