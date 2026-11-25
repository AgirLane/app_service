from datetime import date
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post, Category


def home(request):

    posts = Post.objects.filter(is_published='True')

    return render(request, 'students/home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    Post.objects.filter(pk=pk).update(views=F('views') + 1)
    post.refresh_from_db()
    return render(request, 'students/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'students/post_form.html', {'form': form})


def category_posts(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(is_published=True).select_related('category')  # для ForeignKey
    posts = posts.prefetch_related('tags')  # для ManyToMany
    return render(request, 'students/category.html', {'category': category, 'posts': posts})


def about(request):
    text = 'Im from Atyrau'
    return render(request, 'students/about.html', {'text': text})


def hello(request, name):

    return render(request, 'students/hello.html', {'name': name})

