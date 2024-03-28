from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm

def home_page(request):
    post = Post.objects.all().order_by('-post_date')[:4]
    context = {
        'posts' : post
    }
    return render(request, "./index.html", context)


def all_news_page(request):
    post = Post.objects.all().order_by('-post_date')
    context = {
        'posts' : post
    }
    return render(request, "./news-list.html", context)

def news_detail_page(request,pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post' : post
    }
    return render(request, "./news-detail.html", context )

def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_page")

    else:
        form = NewUserForm()

    context = {
        'form': form
    }

    return render(request,"./sign_up.html", context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("home_page")
    else:
        form=AuthenticationForm

    context = {
        'form': form
    }

    return render(request, "./login.html", context)

def logout_request(request):
    logout(request)
    return redirect("home_page")