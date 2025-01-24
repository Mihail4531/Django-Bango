
from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.filter(is_active=True, is_banner=True).order_by('-created_at')[:3]
    context = {
        'posts': posts,

    }
    return render(request, 'blog/index.html', context)