from django.contrib import admin
from blogs.models import Blog, BlogPost

admin.site.register((Blog, BlogPost))