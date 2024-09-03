from django.urls import path
from . import views  # Import views from the current directory (blog)


urlpatterns = [
    path('', views.post_list, name='post_list'),            # Blog page with filtering
    path('movies/', views.movies_view, name='movies'),      # Movies page
    path('tv-anime/', views.tv_anime_view, name='tv_anime'),# TV/Anime page
    path('new/', views.new_post, name='new_post'),  
    path('player-stats/', views.player_stats_view, name='player_stats'),
]
