from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator
from main.utils import q_search

from news.models import News
from goods.models import Products, Categories


def index(request):
    news = News.objects.all()[:4]
    context = {"news": news}
    return render(request, "main/index.html", context)


def catalog(request):
    categories = Categories.objects.all()
    products = Products.objects.all()
    category_id = request.GET.get("category", 0)
    page = request.GET.get("page", 1)
    query = request.GET.get("q", None)
    if query:
        products = q_search(query)

    if category_id:
        category_id = int(category_id)
        category = Categories.objects.get(pk=category_id)
        products = Products.objects.filter(category=category_id)

    paginator = Paginator(products, 3)
    current_page = paginator.page(page)

    if category_id:
        if category_id == 1:
            context = {
                "category": categories,
                "products": current_page,
                "first": category_id,
                "query": query,
                "choose": category,
            }
        elif category_id == 2:
            context = {
                "category": categories,
                "products": current_page,
                "second": category_id,
                "query": query,
                "choose": category,
            }
        elif category_id == 3:
            context = {
                "category": categories,
                "products": current_page,
                "third": category_id,
                "query": query,
                "choose": category,
            }
        elif category_id == 4:
            context = {
                "category": categories,
                "products": current_page,
                "fourth": category_id,
                "query": query,
                "choose": category,
            }
        elif category_id == 5:
            context = {
                "category": categories,
                "products": current_page,
                "fifth": category_id,
                "query": query,
                "choose": category,
            }
        elif category_id == 6:
            context = {
                "category": categories,
                "products": current_page,
                "sixth": category_id,
                "query": query,
                "choose": category,
            }
    else:
        context = {
            "category": categories,
            "products": current_page,
            "query": query,
        }

    return render(request, "main/catalog.html", context)


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")


# def job(request):
#     return render(request, "main/job.html")
