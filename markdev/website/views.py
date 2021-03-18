from re import error
from rest_framework.response import Response
from rest_framework import generics, status

from .serializers import (
    ArticleSerializer,
    CommentSerializer,
    AuthorSerializer,
    CategoryArticleSerializer,
    TagSerializer,
)
from .models import Article, Comment, Author, CategoryArticle, TagArticle
from .utils.filters import CommentsToArcitleFilter


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects
    filter_backends = (CommentsToArcitleFilter,)


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects


class AuthorView(generics.RetrieveAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects


class CategoryArticleView(generics.ListAPIView):
    serializer_class = CategoryArticleSerializer
    queryset = CategoryArticle.objects


class TagListView(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = TagArticle.objects
    do mergowania