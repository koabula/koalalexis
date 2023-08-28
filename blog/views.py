from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Blogs
import mistune

# Create your views here.
# def blog(request):
#     return render(request, 'blog/blog.html')


def detail(request, blog_id):
    try:
        # post = get_object_or_404(Blogs, pk=blog_id)
        post = Blogs.objects.get(pk=blog_id)
    except Blogs.DoesNotExist:
        raise Http404("Article does not exist")
    post.text = mistune.html(post.text)

    return render(request, 'blog/detail.html', {'post': post})


def blog(request):
    # 获取所有博客文章
    blog_posts = Blogs.objects.all()
    return render(request, 'blog/blog.html', {'blog_posts': blog_posts})
