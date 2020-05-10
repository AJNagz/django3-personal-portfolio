from django.shortcuts import render, get_object_or_404
# import models from Blog class
from .models import Blog

# Create your views here.

def all_blogs(request):
    # store all the Blog class models in a variable
    # blogs = Blog.objects.all()
    # To limit the number of posts us the below code
    blogs = Blog.objects.order_by('-date')[:3]
    # Add a dictionary to the below code
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

    
def detail(request, blog_id):
    # blog variable is getting the blog id
    # here 'Blog' is the class name, 'pk' is the primary key
    # 'blog_id' is the blog id to show
    # get_object_or_404() coming from top
    blog = get_object_or_404(Blog, pk=blog_id)
    # Function will get a id from the url
    # call for detail function is coming from blog/urls.py
    # we have to create a detail.html template in blog/templates/blog
    return render(request, 'blog/detail.html', {'blog':blog})

