from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Post, Group


def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


def show_groups(request):
    #group = get_object_or_404(Group, slug=slug)
    group = Group.objects.all[:11]
    return render(request, "showgroups.html", {"group": group})
