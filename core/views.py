from django.shortcuts import render, get_object_or_404
from core.models import Post

def homepage(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "homepage.html", context)

def post_view(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        "post": post
    }
    return render(request, "post_view.html", context) 