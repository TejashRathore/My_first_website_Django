from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = "home"),
    path('blog-posts',views.blogposts, name = "all-posts"),
    path("blog-posts/<slug:blog>", views.blog_posts, name = "blog-posts")


]   