from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def home(request, *args, **kwargs) -> HttpResponse:
    """Home view"""

    #! Get all posts from database
    posts = Post.objects.all()
    
    #! Context which will be in the Django template
    context = {
        'posts': posts
    }
    return render(request, 'core/index.html', context=context)

