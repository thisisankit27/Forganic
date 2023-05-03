from django.db import models
from django.core.paginator import Paginator

# Create your models here.

class BlogManager(models.Manager):
    def get_paginated(self, page_number, per_page=5):
        blogs = self.get_queryset()
        paginator = Paginator(blogs, per_page)
        return paginator.get_page(page_number)

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    
    objects = BlogManager()
    
    @classmethod
    def create_blog(cls, title, content):
        blog = cls(title=title, content=content)
        blog.save()
        return blog

    def delete_blog(self):
        self.delete()
    
class Comment(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)