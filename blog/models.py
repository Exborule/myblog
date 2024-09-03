from django.db import models
from django.utils import timezone

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('blog', 'Blog'),
        ('movie', 'Movie'),
        ('tv_anime', 'TV/Anime'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='blog')

    def __str__(self):
        return self.title

class PlayerStat(models.Model):
    player = models.CharField(max_length=100)
    age = models.FloatField()
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=10)  # Ensure the field names match
    games_played = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    points = models.IntegerField()
    plus_minus = models.IntegerField()
    penalty_minutes = models.IntegerField()
    even_goals = models.IntegerField()
    power_play_goals = models.IntegerField()
    short_hand_goals = models.IntegerField()
    game_winning_goals = models.IntegerField()
    even_strength = models.IntegerField(default=0)
    power_play = models.IntegerField(default=0)
    short_hand = models.IntegerField()
    shots_on_goal = models.IntegerField()
    shooting_percentage = models.FloatField(null=True, blank=True)
    total_shots_attempted = models.IntegerField()
    time_on_ice = models.FloatField()
    average_time_on_ice = models.FloatField()
    faceoff_wins = models.IntegerField(default=0)
    faceoff_losses = models.IntegerField(default=0)
    faceoff_percentage = models.FloatField(null=True, blank=True)
    blocked_shots = models.IntegerField()
    hits = models.IntegerField()
    takeaways = models.IntegerField()
    giveaways = models.IntegerField()
    awards = models.CharField(max_length=255, blank=True, null=True)  # Ensure this field is included


    def __str__(self):
        return self.player