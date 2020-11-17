from django.views.generic import ListView

from django.http import HttpResponse
from django.shortcuts import render

from .models import Post

class HomeVievs(ListView):
    """Home view"""
    template_name = 'core/index.html'
    queryset = Post.objects.filter(is_active=True)

class PostsVievs(ListView):
    """Posts view"""
    template_name = 'core/index.html'

    def get_queryset(self, **kwargs):
        """Returns active posters post """
        print(self.request.user)
        return Post.objects.filter(is_active=True,
                                    poster=self.request.user)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)