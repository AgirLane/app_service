from datetime import date
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):

    posts = Post.objects.filter(is_published='True')

    return render(request, 'students/home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    return render(request, 'students/post_detail.html', {'post': post})


def about(request):
    text = 'Im from Atyrau'
    return render(request, 'students/about.html', {'text': text})


def hello(request, name):

    return render(request, 'students/hello.html', {'name': name})

