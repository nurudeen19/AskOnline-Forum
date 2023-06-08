from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Category, Post, Comment
from posts.forms import PostForm,CommentForm


def index(request):
	posts = Post.objects.all()
	return render(request,'index.html.j2',{'posts': posts})

@login_required(login_url='/account/login')
def create(request):
	form = PostForm(request.POST, request.FILES)
	if form.is_valid():
		form.save(commit=False).user = request.user
		form.save()
		messages.success(request, 'Post published successfully!') 
		return redirect('home')
	categories = Category.objects.all()
	return render(request,'create.html.j2',{'categories':categories})

def show(request,slug):
	post = Post.objects.filter(slug=slug).get()
	comments = Comment.objects.filter(post=post)
	return render(request, 'show.html.j2', {
		'post':post,
		'comments':comments
	})


def comment(request,slug):
	if request.method == "POST":
		form = CommentForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, "Comment added successfully")
			return redirect(request.GET["next"])
