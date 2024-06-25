from django.urls import path
from .views import *


urlpatterns = [
    # path('login/', LoginView.as_view(template_name='login.html', next_page='/'), name='login')
    path('login/', LoginView.as_view()),
    path('logout/', logout_view),
    path('register', RegisterView.as_view()),
    path('', HomeView.as_view()),
    path('create/', PostCreateView.as_view()),
]
