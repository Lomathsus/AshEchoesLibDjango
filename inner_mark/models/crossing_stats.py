from django.db import models


class CrossingStats(models.Model):
    name = models.CharField(max_length=100)
    unlock_level = models.IntegerField()


class CrossingStatsLevel(models.Model):
    crossing_stats = models.ForeignKey(CrossingStats, on_delete=models.CASCADE)
    level = models.IntegerField()
    value = models.FloatField()
