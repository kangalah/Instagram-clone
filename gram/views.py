from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse
from .models import Post
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostForm


# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,"insta/post_list.html" ,{"posts":posts})



