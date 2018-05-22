from django.shortcuts import render
from django.http import Http404

from .models import Blog

def blogView(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs':blogs})

def blogDetail(request, id):
    try:
        entry = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404('Entry not found')
    return render(request, 'blog/blog_detail.html', {'entry':entry})