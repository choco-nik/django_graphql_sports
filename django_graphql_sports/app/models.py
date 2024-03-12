from django.db import models

class League(models.Model):
    name = models.CharField(max_length=100)
    
class Team(models.Model):
    name = models.CharField(max_length=100)

class Match(models.Model):
    utc_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    home_team_score = models.IntegerField(null=True, blank=True)
    away_team_score = models.IntegerField(null=True, blank=True)
