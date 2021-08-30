from django.urls import path, include

#from .import views
from .views import *
#from .views import AddCategoryView, HomeView, ArticleDetailView, AddPostView, EditPostView, DeletePostView

app_name = 'blog'

urlpatterns = [
  
  path('', HomeView.as_view(), name="home"),
  path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
  path('add-post/', AddPostView.as_view(), name="add-post"),
  path('article/edit/<int:pk>', EditPostView.as_view(), name="article-edit"),
  path('article/<int:pk>/remove', DeletePostView.as_view(), name="article-delete"),
  path('add-category/', AddCategoryView.as_view(), name="add-category"),


]
