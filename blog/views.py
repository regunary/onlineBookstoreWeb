from django.shortcuts import render
from .models import *

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)

def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog-detail.html', context)