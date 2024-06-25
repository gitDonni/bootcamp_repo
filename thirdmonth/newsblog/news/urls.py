from django.urls import path
from .views import home, news_detail



urlpatterns = [
    path('', home),
    path('news_detail/<int:id>', news_detail)
]
