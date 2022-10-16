from django.shortcuts import render

from posts.models import Post


def posts_home(request):
    posts = Post.objects.all().order_by('-date_posted')

    return render(request, 'posts/posts.html', {'posts': posts})


def posts_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'posts/post-detail.html', {'post': post})
