from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound
from django.urls import reverse
blog_names = {
    "python-intro":"Hello user's, You're at the python_intro page.",
    "django-intro": "Hello user's, You're at the django-intro page.",
    "regex":" Hello user's, you're at the regex intro page\nit is use for the file handling in the python.",
    "python-oops": " Hello user's you're at the python oops(object oriented programming)-intro page.",
    "Tkinter":None
}

# Create your views here.

def home(request):
    return render(request,"blog/home_page.html")
   # res_html=render_to_string("blog/index.html")
   # return HttpResponse(res_html)
    
def blogposts(request):
    # Extract all blog names (keys) from the blog_names dictionary as a list
    blog_keys = list(blog_names.keys())

    return render(request, 'blog/blog-posts.html',{'blog':blog_keys})

    # # Iterate through each blog name to generate dynamic links
    # for b in blog_keys:
    #     # Generate the URL path for each blog post using Django's reverse() function with the blog name as an argument
    #     blog_path = reverse("blog-posts", args=[b])
        
    #     # Construct an HTML list item with a hyperlink, capitalizing the blog name for display
    #     list_items += f'<li><a href = "{blog_path}">{b.capitalize()}</a></li>'
    
    # # Wrap all list items in an unordered list (<ul>) HTML tag
    # res_data=f'<ul>{list_items}</ul>'
    # return HttpResponse(res_data)


def blog_posts(request, blog):
    try:
        res = blog_names[blog]
        return render(request, "blog/posts.html",  # this is the way we can make more dynamic templates by using DTL(Django Template Language).G0 and see the title and body of posts.html
    {"blog_text":res, "blog_name":(blog)})
    except Exception:                                       
        raise Http404()


