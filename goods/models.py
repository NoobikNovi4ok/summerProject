from django.forms import forms
from django.db import models
from django.core.files.storage import default_storage
from PIL import Image


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Имя категории")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")
    icon = models.ImageField(upload_to="icon_category", verbose_name="Иконка")

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55, verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")
    photo = models.ImageField(upload_to="products_images", verbose_name="Фотография")
    description = models.CharField(
        max_length=2000, verbose_name="Описание", blank=True, null=True
    )
    notes = models.CharField(
        max_length=700, verbose_name="Примечания", blank=True, null=True
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    cost = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена"
    )
    category = models.ForeignKey(
        to=Categories, on_delete=models.PROTECT, verbose_name="Категория"
    )
    download_file = models.FileField(
        upload_to="excel_table", verbose_name="Excel Таблица", blank=True
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("product_id",)

    def __str__(self):
        return self.name


class Photos(models.Model):
    name = models.CharField(max_length=75, verbose_name="Название")
    product = models.ForeignKey(
        to=Products, on_delete=models.PROTECT, verbose_name="Продукт"
    )
    photogallery = models.ImageField(
        upload_to="products_gallery/", blank=True, verbose_name="Фотогалерея"
    )

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        ordering = ("product_id",)

    def __str__(self):
        return self.name
