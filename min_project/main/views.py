from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def mainpage(request):
    return render(request, 'main/mainpage.html')

def information(request):
    return render(request, 'main/information.html')

def notion(request):
    return render(request, 'main/notion.html')

def talking(request):
    posts=Post.objects.all()
    return render(request, 'main/talking.html', {'posts':posts})

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.hamster = request.POST['hamster']
    new_post.weather = request.POST['weather']
    new_post.body = request.POST['body']

    new_post.save()

    return redirect('detail', new_post.id)

def new(request):
    return render(request, 'main/new.html')

def detail(request,id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'main/detail.html', {'post':post})


