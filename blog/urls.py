from django.urls import path
from . views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView

# from . import views
# urlpatterns = [
#     path('', views.home, name="home"),
# ]

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article-view"),
    path('add-post/', AddPostView.as_view(), name="add-post"),
    path('article/edit-post/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('article/<int:pk>/delete-post', DeletePostView.as_view(), name="delete-post"),
    path('add-category/', AddCategoryView.as_view(), name="add-category"),
    path('category/<str:cats>/', CategoryView, name="category"),
]