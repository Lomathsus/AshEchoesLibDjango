from django.db import models
from .character import Character
from common.abstract_class import BaseModel


class EngravingStat(BaseModel):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="engraving_stats"
    )
    level = models.IntegerField()
    vitality = models.IntegerField()
    defence = models.IntegerField()
    attack = models.IntegerField()
    mastery = models.IntegerField()
    terminal = models.IntegerField()

    class Meta:
        db_table = "character_engraving_stat"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "level"],
                name="unique_character_engraving_stat",
            )
        ]

    def __str__(self):
        return f"{self.character.name}/刻印属性/S{self.level}"
