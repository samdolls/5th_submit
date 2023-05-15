from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile
from main.models import Post


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:mainpage')
        else:
            return render(request, 'accounts/login.html')

    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:mainpage')

def signup(request):
    if request.method == 'POST':

        if request.POST['password'] == request.POST['confirm']:
            
            if request.POST['hamsterlike'] == 'yes':
                user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password'],
                )
                
                nickname = request.POST['nickname'],
                favorite = request.POST['favorite'],
                animal = request.POST['animal'],

                profile = Profile(user=user, nickname = nickname, favorite = favorite, animal = animal)
                profile.save()

                auth.login(request, user)
                return redirect('/')
            elif request.POST['hamsterlike'] == 'no':
                return render(request, 'accounts/signup_hamsterhate.html')
        elif request.POST['password'] != request.POST['confirm']:
            return render(request, 'accounts/signup_wrong.html')
            
            
    
    return render(request, 'accounts/signup.html')