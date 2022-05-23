from django.shortcuts import render
from django.views.generic import ListView

# module, python treate each '.py' as a module. with module, you can import class or function
# in that module to reuse the code
from .models import Post

# Create your views here.

class HomePageView(ListView):
    # we needs a list view here because the data returned from database is a list data type
    # [12, 'hello', true] in python 
    model = Post # it will automatically create an object (list type): post_list
    template_name = "posts/home.html"