from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from xmlrpc.client import Boolean
from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all().order_by('-id'),
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
        return render(request,"createPost.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            user = User(first_name=first_name,
                        last_name=last_name, username=username, email=email, password=password)
            user.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
              if user.is_active:
                  login(request, user)
                  return HttpResponseRedirect("/")
              else:
                  # Return a 'disabled account' error message
                  return redirect('/')
        else:
            return render(request, 'login.html')
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request,'login.html')
