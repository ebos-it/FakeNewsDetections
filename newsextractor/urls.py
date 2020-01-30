from django.urls import path
from .views import (
    NewsArticlesListView,
    NewsArticlesCreateView,
    NewsArticlesDetailView,
    NewsArticlesDeleteView,
    NewsArticlesUpdateView,
)

urlpatterns = [
    path("", NewsArticlesListView.as_view(), name="portal-home"),
    path("new/", NewsArticlesCreateView.as_view(), name="newsarticles-create"),
    path(
        "news/<int:pk>/", NewsArticlesDetailView.as_view(), name="newsarticles-detail"
    ),
    path(
        "news/<int:pk>/delete/",
        NewsArticlesDeleteView.as_view(),
        name="newsarticles-delete",
    ),
    path(
        "news/<int:pk>/update/",
        NewsArticlesUpdateView.as_view(),
        name="newsarticles-update",
    ),
]
