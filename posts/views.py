
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts':posts})

def posts(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'post':post})

def postie(request):
    return render(request, 'postie.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
