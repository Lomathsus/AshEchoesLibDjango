from django.db import models
from .character import Character


class Stats(models.Model):
    level = models.IntegerField()
    health = models.IntegerField()
    attack = models.IntegerField()
    mastery = models.IntegerField()

    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="stats"
    )

    def __str__(self):
        return f"{self.character.name}/位阶属性加成/S{self.level}"
