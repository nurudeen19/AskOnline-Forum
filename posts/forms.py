from django import forms
from posts.models import Category,Post,Comment

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']


class PostForm(forms.ModelForm):
	# title = forms.CharField(label="", widget=forms.)
	# description = forms.TextField(label="", widget=forms.)
	# category = forms.ChoiceField(label="", widget=forms.)

	class Meta:
		model = Post
		fields = ['title','category','description','image']


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['description','post','user']
