from django.contrib import admin
from blog.models import Post
from blog.models import Image
from blog.models import web
from blog.models import video
# Register your models here.

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(web)
admin.site.register(video)