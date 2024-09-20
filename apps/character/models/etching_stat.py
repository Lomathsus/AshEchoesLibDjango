from django.db import models
from .character import Character
from apps.common.abstract_models import TimestampedModel


class EtchingStat(TimestampedModel):
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
        db_table = "character_etching_stat"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "level"],
                name="unique_character_etching_stat",
            )
        ]

    def __str__(self):
        return f"{self.character.name}/刻印属性/S{self.level}"
