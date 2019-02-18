from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    slug = models.SlugField(
        max_length=255, unique=True, null=False, blank=False)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

class Article(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(
        'article.Category', on_delete=models.CASCADE,
        related_name='article_category')
    title = models.CharField(max_length=255)
    content = models.TextField()
