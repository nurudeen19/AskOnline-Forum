from django.db import models
from django.utils.text import slugify
from profiles.models import User


class Category(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField()


	#auto add slug field
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)


	def __str__(self):
		return self.name



class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
	title = models.CharField(max_length=255)
	slug = models.SlugField()
	description = models.TextField()
	image = models.FileField(null=True,upload_to='posts/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	#auto add slug field
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
	description = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	post = models.ForeignKey(Post, on_delete= models.CASCADE, default=None)
	parent= models.ForeignKey("Comment", on_delete=models.CASCADE, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)