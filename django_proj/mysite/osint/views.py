from django.shortcuts import render
from .models import OsintServices

# Create your views here.


def post_list(request):
    posts = OsintServices.objects.all()
    return render(request, 'osint/post/main.html', {'posts': posts})
