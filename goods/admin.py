from ast import Pass
from django import forms
from django.contrib import admin
from goods.models import Categories, Photos, Products
from django.db import models


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "category"]
    search_fields = ["name", "description"]
    list_filter = ["quantity", "category", "cost"]


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ["name", "product_id"]
    search_fields = ["name", "product_id"]
    list_filter = ["name", "product_id"]
