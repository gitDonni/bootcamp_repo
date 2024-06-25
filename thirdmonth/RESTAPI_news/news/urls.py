from django.urls import path
from .views import *
from. import views



urlpatterns = [
    path('', home, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
