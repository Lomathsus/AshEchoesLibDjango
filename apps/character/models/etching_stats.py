from django.db import models
from .character import Character


class EtchingStats(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="etching_stats"
    )
    level = models.IntegerField()
    health = models.IntegerField()
    defence = models.IntegerField()
    attack = models.IntegerField()
    mastery = models.IntegerField()
    terminal = models.IntegerField()

    class Meta:
        db_table = "etching_stats"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "level"], name="unique_etching_stats_level"
            )
        ]

    def __str__(self):
        return f"{self.character.name}/刻印属性/S{self.level}"
