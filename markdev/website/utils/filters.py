from rest_framework import filters


class CommentsToArcitleFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        id_article = request.data.get("id_article")
        return queryset.filter(article=id_article)
