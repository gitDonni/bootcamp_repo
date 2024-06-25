from django.shortcuts import render, redirect
from .models import Product, Banner
from .forms import ApplicationForm


def home(request):
    products = Product.objects.all()[:8]
    banners = Banner.objects.all()
    form = ApplicationForm
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index.html', {'products': products, 'banners': banners, 'form': form})


def contact(request):
    form = ApplicationForm
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'contact.html', {'form': form})


def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})



def why(request):
    return render(request, 'why.html')


def testimonial(request):
    return render(request, 'testimonial.html')
