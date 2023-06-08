from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Category, Post, Comment
from posts.forms import PostForm


def index(request):
	return render(request,'index.html.j2',{})

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