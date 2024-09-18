from django.db import models
from .character import Character


class EtchingStats(models.Model):
    LEVEL_CHOICES = [
        ("s0", "s0"),
        ("s1", "s1"),
        ("s2", "s2"),
        ("s3", "s3"),
        ("s4", "s4"),
        ("s5", "s5"),
        ("s6", "s6"),
    ]

    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="etching_stats"
    )

    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    health = models.IntegerField()
    defence = models.IntegerField()
    attack = models.IntegerField()
    mastery = models.IntegerField()
    terminal = models.IntegerField()

    def __str__(self):
        return f"{self.character.name} etching - {self.level}"
