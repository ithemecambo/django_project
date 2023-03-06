from django.views.generic import ListView
from .models import *


class PostViewPage(ListView):
    model = Post
    template_name = 'posts.html'

