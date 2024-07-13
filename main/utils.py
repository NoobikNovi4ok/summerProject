from django.db.models import Q
from goods.models import Products, Categories


def q_search(query):
    if query.isdigit() and len(query) <= 2:
        return Products.objects.filter(product_id=int(query))

    keywords = [word for word in query.split() if len(word) > 2]

    category = Categories.objects.filter(name__iexact=query).first()
    if category:
        return Products.objects.filter(category=category)

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    return Products.objects.filter(q_objects)
