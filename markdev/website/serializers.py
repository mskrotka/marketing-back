from django.db import models
from rest_framework import serializers

from .models import (
    Article,
    Comment,
    Author,
    CategoryArticle,
    TagArticle,
    Client,
    PortfolioCategory,
)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "title",
            "description",
            "photo",
            "author",
            "category",
            "tag",
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "author",
            "description",
            "parent",
            "date_created",
            "article",
        ]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "name",
            "lastname",
            "photo",
        ]


class CategoryArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryArticle
        fields = [
            "name",
            "parent",
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagArticle
        fields = [
            "name",
        ]
