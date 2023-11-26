from django.urls import path
from . import views
# from .views import HomeView
from .views import HomeView,ArticleDetailView,AddPostView,UPdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView
urlpatterns = [
    path('',HomeView.as_view(), name = "home"),
    # pk => primary_key example url like article/1
    #The name parameter in a Django URL pattern is used to name the URL pattern
    #(name parameter used to create url in html page)
    path('article/<int:pk>',ArticleDetailView.as_view(),name = 'article_details'),
    path('add_post/',AddPostView.as_view(),name="add_post"),
    path('article/edit/<int:pk>',UPdatePostView.as_view(),name="update_post"),
    path('article/delete/<int:pk>',DeletePostView.as_view(),name="delete_post"),
    path('add_category/',AddCategoryView.as_view(),name="add_category"),
    # path('category/<str:cats>/',CategoryView.as_view, name="category"),
    path('category/<str:cats>/', CategoryView.as_view(), name='category'),
    path('category-list/',CategoryListView,name="category-list"),

    
]