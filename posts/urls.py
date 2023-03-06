from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostViewPage.as_view(), name='posts')
]