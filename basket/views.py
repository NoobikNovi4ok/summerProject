import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from goods.models import Products
from basket.models import Basket
from django.template.loader import render_to_string
from basket.utils import get_user_basket


def basket_add(request):
    product_id = request.POST.get("product_id")
    print(product_id)
    product = Products.objects.get(product_id=product_id)

    baskets = Basket.objects.filter(user=request.user, product=product)

    if baskets.exists():
        basket = baskets.first()
        if basket:
            basket.quantity += 1
            basket.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=1)

    user_basket = get_user_basket(request)
    cart_items_html = render_to_string(
        "basket/includes/included_cart.html", {"basket": user_basket}, request=request
    )

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def basket_change(request):
    basket_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")
    change = int(request.POST.get("change"))

    if basket_id and quantity:
        try:
            cart_item = Basket.objects.get(pk=basket_id)
        except Basket.DoesNotExist:
            return JsonResponse({"error": "Товар не найден"}, status=404)

        cart_item.quantity += change  # Изменяем количество
        cart_item.save()

        user_basket = get_user_basket(
            request
        )  # Предполагается, что у вас есть функция get_user_basket
        cart_items_html = render_to_string(
            "basket/includes/included_cart.html",
            {"basket": user_basket},
            request=request,
        )

        response_data = {
            "message": "Количество товаров в корзине успешно обновлено",
            "cart_items_html": cart_items_html,
            "quantity": cart_item.quantity,  # Передаем обновленное количество
        }

        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Неверные данные"}, status=400)

    # basket = Basket.objects.get(basket_id=basket_id)

    # basket.quantity = quantity
    # basket.save()
    # updated_quantity = basket.quantity

    # user_basket = get_user_basket(request)
    # cart_items_html = render_to_string(
    #     "basket/includes/included_cart.html", {"basket": user_basket}, request=request
    # )

    # response_data = {
    #     "message": "Количество изменено",
    #     "cart_items_html": cart_items_html,
    #     "quantity": updated_quantity,
    # }

    # return JsonResponse(response_data)


def basket_remove(request):
    basket_id = request.POST.get("cart_id")
    basket = Basket.objects.get(basket_id=basket_id)
    quantity = basket.quantity
    basket.delete()

    user_basket = get_user_basket(request)
    cart_items_html = render_to_string(
        "basket/includes/included_cart.html", {"basket": user_basket}, request=request
    )

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)
