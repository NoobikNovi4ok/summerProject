from django.db import models

from users.models import User


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")
    photo = models.ImageField(upload_to="news_image", verbose_name="Фотография")
    description = models.CharField(
        max_length=1500, verbose_name="Описание", blank=True, null=True
    )
    small_description = models.CharField(
        max_length=300, verbose_name="Небольшое описание", blank=True, null=True
    )
    include_photo = models.ImageField(upload_to="news_image_include")
    author = models.ForeignKey(to=User, on_delete=models.PROTECT, verbose_name="Автор")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления", null=True
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ("news_id",)

    def __str__(self):
        return self.name
