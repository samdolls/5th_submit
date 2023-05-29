from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Tag
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
    
    if request.user.is_authenticated:
        new_post = Post()
        new_post.title = request.POST['title']
        new_post.writer = request.user
        new_post.pub_date = timezone.now()
        new_post.hamster = request.POST['hamster']
        new_post.weather = request.POST['weather']
        new_post.image = request.FILES.get('image')
        new_post.body = request.POST['body']

        new_post.save()

        words = new_post.body.split(' ')
        tag_list = []

        for word in words:
            if len(word)>0:
                if word[0]=="#":
                    tag_list.append(word[1:])
        
        for tag in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=tag)
            new_post.tags.add(tag.id)

        return redirect('main:detail', new_post.id)
    else:
        return redirect('accounts:login')

def new(request):
    return render(request, 'main/new.html')

def detail(request,id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html', {
            'post':post,
            'comments':comments,
        })
    
    elif request.method == 'POST':
        new_comment = Comment()
        new_comment.post = post
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now()

        new_comment.save()
        
        words = new_comment.content.split(' ')
        tag_list=[]

        for word in words:
            if len(word)>0:
                if word[0] == "#":
                    tag_list.append(word[1:])

        for tag in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=tag)
            new_comment.tags.add(tag.id)

        return redirect('main:detail', id)
    
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('main:detail', comment.post.id)

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post':edit_post})

def update(request, id):
    
    if request.user.is_authenticated:
        update_post = Post.objects.get(id=id)
        if request.user == update_post.writer:
            update_post.title = request.POST['title']
            update_post.writer = request.user
            update_post.pub_date = timezone.now()
            update_post.hamster = request.POST['hamster']
            update_post.weather = request.POST['weather']
            update_post.image = request.FILES.get('image', update_post.image)
            update_post.body = request.POST['body']

            update_post.save()
            
            update_post.tags.clear()
            words = update_post.body.split(' ')
            new_list = []
            
            for word in words:
                if len(word)>0:
                    if word[0] == "#":
                        new_list.append(word[1:])
            for tag in new_list:
                tag, boolean = Tag.objects.get_or_create(name=tag)
                update_post.tags.add(tag.id)


            return redirect('main:detail', update_post.id)
    return redirect('accounts:login')

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()

    return redirect('main:talking')

def tag_list(request):
    empty_tags = Tag.objects.filter(posts = None, comments = None)
    empty_tags.delete()
    tags = Tag.objects.all()
    return render(request, 'main/tag_list.html', {
        'tags':tags,
        })

def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, id = tag_id)
    posts = tag.posts.all()
    comments = tag.comments.all()
    return render(request, 'main/tag_posts.html', {
        'tag':tag,
        'posts':posts,
        'comments':comments,
    })


