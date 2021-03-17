from uuid import uuid4

from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    photo = models.ImageField(upload_to="author")

    def __str__(self):
        return f"{self.name} {self.lastname}"


class CategoryArticle(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=64)


class Article(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    photo = models.ImageField(upload_to="article")
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(CategoryArticle)
    tag = models.ManyToManyField(Tag)


class Comment(models.Model):
    author = models.CharField(max_length=32)
    description = models.TextField()
    accepted = models.BooleanField(default=False)
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    date_created = models.DateTimeField(auto_now_add=True)


class Client(models.Model):
    name = models.CharField(max_length=128)
    logo = models.ImageField(upload_to="client_logo")


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=128)


class PortfolioTechnology(models.Model):
    name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to="technology")


class PortfolioType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    type = models.ForeignKey(PortfolioType, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)
    time_work = models.SmallIntegerField(default=0, null=True, blank=True)
    index = models.BooleanField(default=False)
    site = models.CharField(max_length=128, null=True, blank=True)
    technology = models.ManyToManyField(PortfolioTechnology)

    photo_thumbnail = models.ImageField(upload_to="portfolio")
    photo1 = models.ImageField(upload_to="portfolio", null=True, blank=True)
    photo2 = models.ImageField(upload_to="portfolio", null=True, blank=True)
    photo3 = models.ImageField(upload_to="portfolio", null=True, blank=True)
    photo4 = models.ImageField(upload_to="portfolio", null=True, blank=True)


class Newsletter(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    activate = models.BooleanField(default=False)
    secret_number = models.UUIDField(default=uuid4, unique=True, editable=False)
    date_activate = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)