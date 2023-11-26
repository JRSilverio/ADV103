from django.urls import path
from .views import TagListView, CategoryListView, CategoryDetailView, TagDetailView, AlbumListView, AlbumDetailView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('home/', login_required(views.home, login_url='/api/login/'), name='home'),
    path('albums/tags/',  login_required(TagListView.as_view(), login_url='/api/login/'), name='tag-list'),
    path('albums/category/', login_required(CategoryListView.as_view(), login_url='/api/login/'), name='category-list'),
    path('albums/categories/<int:pk>/', login_required(CategoryDetailView.as_view(), login_url='/api/login/'), name='category-detail'),
    path('albums/tags/<int:pk>/', login_required(TagDetailView.as_view(), login_url='/api/login/'), name='tag-detail'),
    path('albums/', login_required(AlbumListView.as_view(), login_url='/api/login/'), name='article-list'),
    path('albums/<int:pk>/', login_required(AlbumDetailView.as_view(), login_url='/api/login/'), name='article-detail'),
]
