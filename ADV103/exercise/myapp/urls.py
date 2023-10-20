from django.urls import path
from .views import TagListCreateView, CategoryListCreateView, CategoryDetailView, TagDetailView, ArticleListView, ArticleDetailView

urlpatterns = [
    path('articles/tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('articles/category/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('articles/categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('articles/tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
