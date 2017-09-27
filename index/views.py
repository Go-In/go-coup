from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index/index.html', {})

def detail(request):
    return render(request, 'index/detail.html', {})

def profile(request):
    return render(request, 'index/profile.html', {})

def cart(request):
    return render(request, 'index/cart.html', {})