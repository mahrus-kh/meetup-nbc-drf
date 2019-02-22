from rest_framework import serializers, validators

from article.models import Category, Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'pk',
            'slug',
            'category',
        )
        read_only_fields= ('pk','slug',)


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'pk',
            'slug',
            'category',
            'title',
            'content',
        )
        read_only_fields= ('pk','slug',)


class ArticleListSerializer(ArticleSerializer):
    category = CategorySerializer()


class CategoryArticlesSerializer(serializers.ModelSerializer):
    article_category = ArticleSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'pk',
            'slug',
            'category',
            'article_category'
        )
