from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = UserRegisterRecipients(name = name, email = email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect(index)
    current_user = request.user
    all_images = Image.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    profile = Profile.objects.all()
    print(likes)
    context = {
        'posts': Post.objects.all()
    }
    return render(request,"insta/post_list.html" ,{"posts":posts, "letterForm":form})

@login_required(login_url='login')
def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
            return redirect('index')
    else:
        form = ImageForm()


    return render(request,'image.html',locals())

def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        print(results)
        return redirect(index)

        return render(request,'results.html',locals())

    

def comment(request,image_id):
    current_user=request.user
    image = Image.objects.get(id=image_id)
    profile_owner = User.objects.get(username=current_user)
    comments = Comment.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.comment_owner = current_user
            comment.save()

            print(comments)


        return redirect(index)

    else:
        form = CommentForm()

    return render(request, 'comment.html', locals())

def follow(request,user_id):
    users=User.objects.get(id=user_id)
    follow = Follow.objects.add_follower(request.user, users)

    return redirect('/profile/', locals())

def like(request, image_id):
    current_user = request.user
    image=Image.objects.get(id=image_id)
    new_like,created= Likes.objects.get_or_create(liker=current_user, image=image)
    new_like.save()

    return redirect('index')

class PostListView(ListView):
    model = Post
    template_name = 'insta/post_list.html'
    ordering = ['-created_date']
    context_object_name = 'posts'

class UserPostListView(ListView):
    model = Post
    template_name = 'insta/user_posts.html'
    context_object_name = 'posts'

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'insta/post_detail.html'
    context_object_name = 'posts'
    

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['image','caption']
    template_name = 'insta/post_form.html'
    success_url = '/'
    

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'insta/post_form.html'
    context_object_name = 'posts'
    fields = ['caption']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
   
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    template_name = 'insta/post_detail.html'
    context_object_name = 'posts'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    

