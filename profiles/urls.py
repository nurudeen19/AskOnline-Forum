from django.urls import path
from profiles import views
from django.contrib.auth import views as auth_views
from profiles.forms import CustomLoginForm

#,authentication_form=CustomLoginForm
            
urlpatterns = [
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name= 'login.html.j2',authentication_form=CustomLoginForm), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
]