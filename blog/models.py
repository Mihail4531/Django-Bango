
from collections import defaultdict

from django.db import models

# Model Category
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории", blank=False)
    slug = models.SlugField(max_length=255, verbose_name="URL - ссылка", unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

# Model tag


# Model Post
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, verbose_name="Категория")
    title = models.CharField(max_length=255, verbose_name="Название поста", blank=False)
    slug = models.SlugField(max_length=255, verbose_name="URL - ссылка", unique=True)
    description = models.TextField(verbose_name="Краткое описание", blank=False)
    content = models.TextField(verbose_name="Контент", blank=False)
    image = models.ImageField(upload_to="posts/", verbose_name="Изображение", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    is_banner = models.BooleanField(default=False, verbose_name="Отображать в баннере", help_text="Данная запись будет отображаться в баннере на главной странице")
    is_recent = models.BooleanField(default=False, verbose_name="Новая запись", help_text="Данная запись будет отображаться в разделе новинки")
    is_featured = models.BooleanField(default=False, verbose_name="Рекомендуемая запись")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title

