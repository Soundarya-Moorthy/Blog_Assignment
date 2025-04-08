from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blogapp/home.html', {'posts': posts})

def detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blogapp/detail.html', {'blog': blog})