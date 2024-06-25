from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('product/detail/<int:id>', product_detail),
]