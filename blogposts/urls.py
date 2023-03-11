from django.urls import path
from blogposts import views


urlpatterns = [
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog-detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
]