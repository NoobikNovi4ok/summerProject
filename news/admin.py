from ast import Pass
from django.contrib import admin
from news.models import News


@admin.register(News)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "small_description"]
    search_fields = ["name", "author"]
    list_filter = ["author"]
