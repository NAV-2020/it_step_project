from django.urls import path

from .views import (
    PostsVievs,
    HomeVievs,
)

app_name = 'core'                     

urlpatterns = [
    path('', HomeVievs.as_view(), name='home'),
    path('posts/', PostsVievs.as_view(), name='my_posts'),
]