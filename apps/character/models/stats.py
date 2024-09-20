from django.db import models
from .character import Character


class Stats(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="stats"
    )
    level = models.IntegerField()
    health = models.IntegerField()
    attack = models.IntegerField()
    mastery = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "level"], name="unique_character_stats_level"
            )
        ]

    def __str__(self):
        return f"{self.character.name}/位阶属性加成/S{self.level}"
