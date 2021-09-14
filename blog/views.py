from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post, Category
from . forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

# Function Based Views
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.title().replace('-', ' '))
    return render(request, 'category.html', {'cats':cats.title().replace('-', ' '),'category_posts':category_posts})

# Class Based Views
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    # ordering = ['-id']

class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'

class AddPostView(CreateView):
    model = Post
    form_class  = PostForm
    template_name = 'add_post.html'
    # fields = "__all__"

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = "__all__"

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ('title', 'title_tag', 'body')    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')