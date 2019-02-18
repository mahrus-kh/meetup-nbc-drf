from django.urls import path
from article.api.view import (
    CategoryView,
    ArticleListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleView,
    CategoryArticlesView,
)


urlpatterns = [
    path('category/', CategoryView.as_view(
        {'get':'list', 'post': 'create'})
    ),
    path('category/<slug:slug>/', CategoryView.as_view(
            {'get':'retrieve', 'put': 'update', 'delete': 'destroy'}
        )
    ),

    path('category/<slug:slug>/articles/', CategoryArticlesView.as_view()),

    path('article/', ArticleListView.as_view()),
    path('article/create/', ArticleCreateView.as_view()),
    path('article/<slug:slug>/update/', ArticleUpdateView.as_view()),
    path('article/<slug:slug>/retrieve/', ArticleView.as_view()),
    path('article/<slug:slug>/destroy/', ArticleView.as_view())
]
