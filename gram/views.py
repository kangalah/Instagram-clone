from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse
from .models import Post
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostForm,SignUpForm


# Create your views here.
@login_required(login_url='login')
def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpRsponseRedirect(request.path_info)
        else:
            form = PostForm()
        params = {
            'posts':posts,
            'form':form,
        }
    return render(request,"insta/post_list.html" ,{"posts":posts})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

