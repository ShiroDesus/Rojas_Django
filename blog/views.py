from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Post
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.http import JsonResponse
import os
from .models import Post
from .forms import PostForm
from django.urls import reverse
# Create your views here.

def blog_list(request):
    post = Post.objects.all()
    context = {

        'blog_list':post
    }
    return render(request, "blog/blog_list.html",context)

def blog_detail(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == 'GET':
        context = {
            'blog_detail': post
        }    
        return render(request, "blog/blog_detail.html", context)

def like_post(request, id):
    post = Post.objects.get(id=id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse('blog_list'))

def blog_delete(request, id):
    each_post = Post.objects.get(id=id)
    each_post.delete()
    return HttpResponseRedirect('/posts/')

def blog_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts/')
    content = {
        'form': form
    }
    return render(request,"blog/blog_create.html", content)

def blog_update(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
    # except ValueError:
        return HttpResponse("Post not found.", status=404)
    
    else:
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/posts/')
        context = {
            "form": form,
            'form_type': 'Create'
        }
        return render(request, "blog/blog_create.html", context)