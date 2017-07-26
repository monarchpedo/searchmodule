from django.conf.urls import patterns, url, include
from django.views.generic import ListView
from blog.models import Post


urlpatterns = [
          url(r'^','blog.views.blogs', name='blogs'),

]
