from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index/index.html', {})

def detail(request):
    return render(request, 'index/detail.html', {})