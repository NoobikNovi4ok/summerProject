from django.shortcuts import render, redirect
from goods.models import Photos, Products
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def goods_get(request, slug=None):
    producti = Products.objects.get(slug=slug)
    photos = Photos.objects.filter(product_id=producti.product_id)
    context = {
        "product": producti,
        "photos": photos,
    }
    return render(request, "goods/goods.html", context)


def download_file(request, product_id):
    product = get_object_or_404(Products, product_id=product_id)
    response = HttpResponse(
        product.download_file.read(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = 'attachment; filename="{}"'.format(
        product.download_file.name
    )
    return response
