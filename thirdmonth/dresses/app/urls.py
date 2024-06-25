from django.urls import path
from .views import *



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
    ]
