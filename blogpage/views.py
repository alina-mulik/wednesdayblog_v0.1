from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def showblog(request):
    posts = BlogPost.objects
    return render(request, 'blogpage/blog.html', {'posts': posts})

def post_details (request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blogpage/post_details.html', {'post': post})
