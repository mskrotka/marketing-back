from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

from .views import (
    ArticleListView,
    CategoryArticleView,
    CommentListView,
    AuthorListView,
    AuthorView,
    TagListView,
    ContactFormView,
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

    # Pjedyńcze instacje - POST
    path("contact-form/", ContactFormView.as_view(), name="contact_form"),

    path("swagger/", get_swagger_view(title='michal-swiderski.pl'))
]
