from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect
from .forms import PostForm
import json
from blog.models import PlayerStat


# Blog View
def post_list(request):
    category = request.GET.get('category')
    if category and category in dict(Post.CATEGORY_CHOICES).keys():
        posts = Post.objects.filter(category=category)
    else:
        posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def movies_view(request):
    posts = Post.objects.filter(category='movie')
    return render(request, 'blog/post_list.html', {'posts': posts})

def tv_anime_view(request):
    posts = Post.objects.filter(category='tv_anime')
    return render(request, 'blog/post_list.html', {'posts': posts})

def hockey_view(request):
    return render(request, 'blog/hockey.html')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the list of posts after saving
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})

def player_stats_view(request):
    player_stats = PlayerStat.objects.all()  # Fetch all player stats
    return render(request, 'Blog/player_stats.html', {'player_stats': player_stats})
