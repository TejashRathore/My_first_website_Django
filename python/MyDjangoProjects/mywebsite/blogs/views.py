from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
blog_names = {
    "python-intro":"<h1>Hello user's, You're at the python_intro page.</h1>",
    "django-intro": "<h1>Hello user's, You're at the django-intro page.</h1>",
    "regex":"<h1> Hello user's, you're at the regex intro page\nit is use for the file handling in the python.</h1>",
    "python-oops": "<h1> Hello user's you're at the python oops(object oriented programming)-intro page.</h1>",

}

# Create your views here.

def home(request):
    res_html=render_to_string("blog/index.html")
    return HttpResponse(res_html)

def blogposts(request):
    list_items = ""
    blog_keys = list(blog_names.keys())
    for b in blog_keys:
        blog_path = reverse("blog-posts", args=[b])
        list_items += f'<li><a href = "{blog_path}">{b.capitalize()}</a></li>'
    res_data=f'<ul>{list_items}</ul>'
    return HttpResponse(res_data)


def blog_posts(request, blog):
    try:
        res = blog_names[blog]
    except Exception:
        return HttpResponseNotFound("<h1>Blog post not found.</h1>")
    else:
         return HttpResponse(res)


def blogposts_by_number(request, blog):
    return HttpResponse(blog)