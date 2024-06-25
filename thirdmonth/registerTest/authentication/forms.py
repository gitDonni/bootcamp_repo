from django import forms
from django.contrib.auth.forms import UserCreationForm

from authentication.models import Post


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField()


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='Почтa')
    first_name = forms.CharField(help_text='Имя')



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
