from django.urls import path, include

from .views import (
    ArticleListView,
    CategoryArticleView,
    CommentListView,
    AuthorListView,
    AuthorView,
    TagListView,
)

urlpatterns = [
    # Listy instancji - GET, POST
    path("articles/", ArticleListView.as_view(), name="articles_list"),
    path("comments/", CommentListView.as_view(), name="comments_list"),
    # Listy instancji - GET
    path("authors/", AuthorListView.as_view(), name="authors_list"),
    path("catgory-article/", CategoryArticleView.as_view(), name="categories_article"),
    path("all-tags/", TagListView.as_view(), name="all_tags_list"),
    # Pojedyńcze instancje - GET
    path("author/<int:pk>", AuthorView.as_view(), name="author"),
]
