from django.urls import path
from . import views

urlpatterns = [
    path("blog", views.BlogPost, name="blog"),
    path("post/<str:pk>", views.Post, name="post"),
]
