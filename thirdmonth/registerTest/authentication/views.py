from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import LoginForm, CustomRegisterForm, PostForm
from django.contrib.auth.forms import UserCreationForm

from .models import Post


class RegisterView(generic.FormView):
    form_class = CustomRegisterForm
    template_name = 'login.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User(username=form.clean_username(), email=request.POST.get('email'), first_name=request.POST.get('first_name'))
            user.save()
            user.set_password(form.clean_password2())
            user.save()
            login(request, user)
            return redirect('/')
        return redirect('/register')


class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('/')
        return redirect('/login/')



# def login_view(request):
#     context = {'form': LoginForm}
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
#         if user:
#             login(request, user)
#             return redirect('/')
#     return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')



class HomeView(generic.ListView):
    template_name = 'index.html'
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'


class PostCreateView(generic.CreateView, LoginRequiredMixin):
    template_name = 'create.html'
    model = Post
    form_class = PostForm
    context_object_name = 'form'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('/login/')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('/')
