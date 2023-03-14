from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blogs.html'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'blog_create.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog_update.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blogs')

