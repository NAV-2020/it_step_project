from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def home(request, *args, **kwargs) -> HttpResponse:
    """Home view"""
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'core/index.html', context=context)

