from django.urls import path

from .views import home as home_view


urlpatterns = [
    path('home/', home_view)
]