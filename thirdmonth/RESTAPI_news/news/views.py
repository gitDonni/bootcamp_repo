from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from .models import *
from django.utils import timezone
from rest_framework import generics, viewsets

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import NewsSerializers


def home(request):
    posts = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'index.html', {'home': home, 'posts': posts})




def post_detail(request, pk):
    post = get_object_or_404(News, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


# class NewsViewSet(viewsets.ModelViewSet):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializers
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.title})


class NewsAPIList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )



class NewsAPIUpdate(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    permission_classes = (IsAuthenticated, )


class NewsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    permission_classes = (IsAdminOrReadOnly, )

