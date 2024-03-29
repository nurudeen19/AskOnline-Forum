from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from django.contrib.auth import authenticate
from posts.models import Post


@login_required(login_url='/account/login')
def home(request):
	posts = Post.objects.filter(user =request.user)
	return render(request, 'home.html.j2',{'posts': posts})

	
def register(request):
	if request.method == "POST":
		form = CustomUserForm(request.POST)
		if form.is_valid():
			form.save()
			# username = request.POST.get("email")
			# password = request.POST.get("password1")
			# user = authenticate(username=username, password=password)
			return redirect('login')
	else:
		form = CustomUserForm()
	return render(request, 'register.html.j2',{'form':form})


