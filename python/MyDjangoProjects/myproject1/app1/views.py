from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
'''views are the area where you write all the functioning codes or functions that you want to implement 
on the web page to process the user's request'''

def blogs(request):
    return HttpResponse("Hello World!!!, this is my first ever django project where i learn about the"
                        " urls and views and learn how to made a project and run it on a command prompt."
                        "\nThank you for coming here...")
