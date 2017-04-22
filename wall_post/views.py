from django.shortcuts import render, redirect
from django.http import HttpResponse
from wall_post.models import WallPost


def index(request):

    wall_post = WallPost.objects.all().order_by('-id')

    if request.method == 'POST':
        name = request.POST.get('name')
        post = request.POST.get('post')
        if name and post:
            WallPost.objects.create(name=name, post=post)
    context = {
        'wall_post': wall_post,
    }
    return render(request, 'wall_post/index.html', context)
