from django.db import models
from .character import Character


class EtchingStats(models.Model):
    level = models.IntegerField()
    health = models.IntegerField()
    defence = models.IntegerField()
    attack = models.IntegerField()
    mastery = models.IntegerField()
    terminal = models.IntegerField()

    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="etching_stats"
    )

    def __str__(self):
        return f"{self.character.name}/刻印属性/S{self.level}"
