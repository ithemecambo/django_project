from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blogs.html'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'
