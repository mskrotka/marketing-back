from django.contrib import admin

from .models import (
    Author,
    CategoryArticle,
    TagArticle,
    Article,
    PortfolioCategory,
    Comment,
    Client,
    Portfolio,
    PortfolioTechnology,
    Newsletter,
    ContactForm,
)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    exclude = []
    list_display = [
        "name",
        "lastname",
    ]
    list_filter = ("name",)
    search_fields = (
        "name",
        "last_name",
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    exclude = []
    list_display = [
        "title",
        "date_created",
        "author",
    ]
    list_filter = [
        "title",
        "description",
    ]
    search_fields = (
        "title",
        "description",
    )


@admin.register(CategoryArticle)
class CategoryArticleAdmin(admin.ModelAdmin):
    exclude = []
    list_display = [
        "name",
    ]
    list_filter = [
        "name",
    ]
    search_fields = ("name",)


@admin.register(TagArticle)
class TagAdmin(admin.ModelAdmin):
    exclude = []
    list_display = [
        "name",
    ]
    list_filter = [
        "name",
    ]
    search_fields = ("name",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    exclude = []
    list_display = [
        "author",
        "date_created",
        "accepted",
    ]
    list_filter = [
        "accepted",
        "article",
    ]
    search_fields = (
        "author",
        "description",
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    exclude = []
    list_display = [
        "name",
    ]
    list_filter = [
        "name",
    ]
    search_fields = ("name",)


@admin.register(Portfolio)
class ProtfolioAdmin(admin.ModelAdmin):
    exclude = []
    list_display = [
        "client",
        "index",
    ]
    list_filter = [
        "index",
    ]
    search_fields = (
        "client",
        "description",
    )


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    exclude = []
    list_display = [
        "name",
    ]
    list_filter = [
        "name",
    ]
    search_fields = ("name",)


@admin.register(PortfolioTechnology)
class PortfolioTechnologyAdmin(admin.ModelAdmin):
    exclude = []
    list_display = [
        "name",
    ]
    list_filter = [
        "name",
    ]
    search_fields = ("name",)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    exclude = []
    list_display = [
        "email",
        "date_created",
        "activate",
    ]
    list_filter = [
        "activate",
    ]
    search_fields = ("email",)


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    exclude = []
    list_display = [
        "email",
    ]
    list_filter = [
        "email",
    ]
    search_fields = ("email",)