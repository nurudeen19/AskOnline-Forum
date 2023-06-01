from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin



class UserManager(BaseUserManager):

	def create_user(self, email,username, first_name, last_name, password=None):
		#create new user
		if not email:
			raise ValueError("Please enter a valid email address")
			email = self.normalise_email(email)
			user = self.model(email=email,username=username, first_name=first_name, last_name=last_name)
			user.set_password(password)
			user.save()

			return user
		


class User(AbstractBaseUser, PermissionsMixin):
	#define custom fields for user model
	email= models.EmailField(max_length=255,unique=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	username = models.CharField(max_length=150,unique=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	#use email as defult username
	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def get_full_name(self):
		#get user's full name
		return f"{self.first_name} {self.last_name}"


	def get_short_name(self):
		return f"{self.first_name}"


	def get_username(self):
		return self.username



