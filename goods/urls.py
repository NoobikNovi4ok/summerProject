from django.urls import path

from goods.views import goods_get, download_file

urlpatterns = [
    path(r"<slug:slug>", goods_get),
    path(r"<int:product_id>/", download_file, name="download_file"),
]
