from datetime import date 
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound
from django.urls import reverse
blog_details = [
    {
            "slug":"python-intro",
            "image":"python.jpg",
            "date": date(year=2026, month=9, day=20),
            "title":"Python Introduction",
            "preview":"""python is an open source high level language that is used widly by many users and programmers 
            Application of python are software development, Data science, AI, Ml etc.""",
            "content":"""Python drives everything from web development and task automation to advanced data science and machine learning.
            Its clean, readable syntax mirrors natural English, making it one of the easiest programming languages to learn. 
            Backed by a huge global community and vast library ecosystem, Python lets you build complex applications quickly."""
    },
    {
            "slug": "django-intro",
            "image": "django.jpg",
            "date": date(year=2026, month=9, day=21),
            "title": "Django Introduction",
            "preview": """Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, it takes care of much of the hassle of web development.""",
            "content": """Django follows the Model-View-Template (MVT) architectural pattern and emphasizes reusability, rapid prototyping, and the 'Don't Repeat Yourself' (DRY) principle.
            It comes with a built-in admin interface, robust database ORM, and integrated security features to protect against common web vulnerabilities out of the box."""
            },
            {
            "slug": "python-oops",
            "image": "oops.png",
            "date": date(year=2026, month=9, day=19),
            "title": "Python Object-Oriented Programming",
            "preview": """Object-Oriented Programming (OOP) in Python is a programming paradigm that uses objects and classes to structure software program design into reusable code patterns.""",
            "content": """Python fully supports object-oriented programming concepts including classes, objects, inheritance, encapsulation, polymorphism, and abstraction.
            By organizing code into logical components, OOP makes complex software systems easier to scale, maintain, and debug over time."""
    }
                ]
{
    "python-intro":"Hello user's, You're at the python_intro page.",
    "django-intro": "Hello user's, You're at the django-intro page.",
    "regex":" Hello user's, you're at the regex intro page\nit is use for the file handling in the python.",
    "python-oops": " Hello user's you're at the python oops(object oriented programming)-intro page.",
    "Tkinter":None
}


# Create your views here.

def home(request):
    sorted_blog = sorted(blog_details, key = lambda post:post["date"], reverse = True )
    latest_blog = sorted_blog[0:2]
    return render(request,"blog/home_page.html", {"latest_blog":latest_blog})

def blogposts(request):
    return render(request, 'blog/blog-posts.html',{'blog':blog_details})



def blog_posts(request, blog):
    try:
        res = blog_details[blog]
        return render(request, "blog/posts.html",  # this is the way we can make more dynamic templates by using DTL(Django Template Language).G0 and see the title and body of posts.html
    {"blog_text":res, "blog_name":(blog)})
    except Exception:                                       
        raise Http404()


