from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from xmlrpc.client import Boolean
from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all().order_by('-id')[:20],
        'r': User.objects.filter(is_superuser=False)
    }
    return render(request, 'index.html', context)

def createPosts(request):
    if request.method == 'POST':
        content = request.POST['content']
        image = request.FILES.get('image')

        if content:
            posts = Post(content=content, image=image, author=request.user)
            posts.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return render(request,"createpost.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            print(password)
            if User.objects.filter(username=username).exists():
                return redirect('/')
            else:
                user = User.objects.create_user(first_name=first_name,
                        last_name=last_name, username=username, email=email, password=password)
                user.save()
                return redirect('/')
        else:
            print("password not equal")
            return redirect('/')
    else:
        return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("user not found")
            return render(request, 'register.html')
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request,'login.html')
