from django.shortcuts import render
from .models import Blog


def bloglist(request):
    blogs = Blog.objects.all().order_by('-created')
    return render(request, 'blog/bloglist.html', {'blogs': blogs})
