from datetime import date
from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    posts = [
        {'title': 'Первый пост', 'text': 'Начинаю изучать Django.'},
        {'title': 'Второй пост', 'text': 'Шаблоны это удобно.'},
        {'title': 'Третий пост', 'text': ''},
    ]

    return render(request, 'students/home.html', {'posts': posts})

def about(request):
    text = 'Im from Atyrau'
    return render(request, 'students/about.html', {'text': text})

def hello(request, name):

    return render(request, 'students/hello.html', {'name': name})

