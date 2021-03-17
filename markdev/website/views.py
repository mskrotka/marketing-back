from re import error
from rest_framework.response import Response
from rest_framework import generics, status

from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment
from .utils.filters import CommentsToArcitleFilter


class ArticleListViews(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects


class CommentListViews(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects
    filter_backends = (CommentsToArcitleFilter,)
