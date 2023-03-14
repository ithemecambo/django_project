from django.urls import path
from blogposts import views


urlpatterns = [
    path('', views.BlogListView.as_view(), name='blogs'),
    path('blog-create/', views.BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/update', views.BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog-delete'),
    path('blog-detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
]