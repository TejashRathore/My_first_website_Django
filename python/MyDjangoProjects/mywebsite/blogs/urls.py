from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('blog-posts',views.blogposts),
    path("blog-posts/<slug:blog>", views.blog_posts,name = "blog-posts")


]   