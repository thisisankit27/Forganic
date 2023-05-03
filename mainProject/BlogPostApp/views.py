from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Blogs, Comment
# Create your views here.

def add_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        blog = Blogs.create_blog(title=title, content=content)
        return redirect('blog_list')
    return render(request, 'admin/add_blog.html')

def delete_blog(request, id):
    blog = Blogs.objects.get(id=id)
    blog.delete_blog()
    return redirect('blog_list')

def BlogPost(request):
    page_number = request.GET.get('page')
    blogs = Blogs.objects.get_paginated(page_number)
    return render(request, "StoryBook/BlogPost.html", {'blogs': blogs})

def Post(request,pk):
    return render(request, "StoryBook/SinglePost.html")