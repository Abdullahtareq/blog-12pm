from django.shortcuts import render

from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    c = {'post_list': posts,}
    return render(request, 'post_list.html', c)

def pub_post_list(request):
    posts = Post.objects.filter(status=1)
    c = {'post_list': posts,}
    return render(request, 'post_list.html', c)
    
def draft_post_list(request):
    posts = Post.objects.filter(status=0)
    c = {'post_list': posts,}
    return render(request, 'post_list.html', c)