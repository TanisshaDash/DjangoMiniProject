from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Like

def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def likePost(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        liked_post = Post.objects.get(pk=post_id)
        Like.objects.create(post=liked_post)
        return HttpResponse("Liked!")
    return HttpResponse("Invalid request.")