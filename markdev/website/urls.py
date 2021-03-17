from django.urls import path, include

from .views import ArticleListViews, CommentListViews

urlpatterns = [
    # Listy instancji - GET, POST
    path("articles/", ArticleListViews.as_view(), name="articles_list"),
    path("comments/", CommentListViews.as_view(), name="comments_list"),
    # Pojedyńcze instancje - GET, PUT, PATCH, DELETE
]
