from django.db import models
from .character import Character
from apps.common.abstract_models import TimestampedModel


class Stat(TimestampedModel):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="stats"
    )
    level = models.IntegerField()
    health = models.IntegerField()
    attack = models.IntegerField()
    mastery = models.IntegerField()

    class Meta:
        db_table = "character_stat"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "level"], name="unique_character_stat"
            )
        ]

    def __str__(self):
        return f"{self.character.name}/位阶属性加成/S{self.level}"
