from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import Category, Post
from .forms import  PostForm, EditForm

# Create your views here.

def posts(request):
    return render(request,'blog/home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-id']
    paginate_by = 10

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('blog:home')
    #fields = '__all__'

class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/edit_post.html'
    success_url = reverse_lazy('blog:home')
    #fields = ('title','body')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:home')


class AddCategoryView(CreateView):
    model = Category
   # form_class = CategoryForm
    template_name = 'blog/add_category.html'
    fields = '__all__'
   
  