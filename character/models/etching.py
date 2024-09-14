from django.db import models
from .character import Character


class Etching(models.Model):
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
        Character, on_delete=models.CASCADE, related_name="stats"
    )

    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    health = models.PositiveIntegerField()
    defence = models.PositiveIntegerField()
    attack = models.PositiveIntegerField()
    mastery = models.PositiveIntegerField()
    terminal = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.character.name} etching - {self.level}"
