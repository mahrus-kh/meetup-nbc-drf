from slugify import slugify
from rest_framework import generics, viewsets

from article.models import Category, Article
from article.api.serializers import (
    CategorySerializer,
    ArticleSerializer,
    ArticleListSerializer,
    CategoryArticlesSerializer,
)


class CategoryView(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # lookup_field = 'slug'
    #
    # def perform_create(self, serializer):
    #     serializer.save(
    #         slug = slugify(self.request.data.get('category'))
    #     )
    #
    # def perform_update(self, serializer):
    #     serializer.save(
    #         slug = slugify(self.request.data.get('category'))
    #     )


class CategoryArticlesView(generics.RetrieveAPIView):

    serializer_class = CategoryArticlesSerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'


class ArticleListView(generics.ListAPIView):

    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()


class ArticleCreateView(generics.CreateAPIView):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            slug = slugify(self.request.data.get('title'))
        )


class ArticleUpdateView(generics.UpdateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(
            slug = slugify(self.request.data.get('title'))
        )


class ArticleView(generics.RetrieveDestroyAPIView):

    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()
    lookup_field = 'slug'
