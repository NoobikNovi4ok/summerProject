from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("product/", include("goods.urls")),
    path("news/", include("news.urls")),
    path("user/", include("users.urls", namespace="user")),
    path("basket/", include("basket.urls", namespace="basket")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("download/", include("goods.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
