from django.shortcuts import render
from .models import OsintServices
from .models import Category

# Create your views here.


def post_list(request):
    posts = OsintServices.objects.all()
    menu = Category.objects.all()
    return render(request, 'osint/post/main.html', {
        'posts': posts,
        "menu": menu,
    })


def post_category(request, url):
    posts = OsintServices.objects.filter(category__url=url)
    menu = Category.objects.all()
    return render(request, 'osint/post/main.html', {
        'posts': posts,
        "menu": menu,
    })