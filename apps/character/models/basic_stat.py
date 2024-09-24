from django.db import models
from .character import Character
from common.abstract_class import BaseModel


class BasicStat(BaseModel):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="basic_stats"
    )
    level = models.IntegerField()
    vitality = models.IntegerField()
    attack = models.IntegerField()
    mastery = models.IntegerField()

    class Meta:
        db_table = "character_stat"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "level"], name="unique_character_basic_stat"
            )
        ]

    def __str__(self):
        return f"{self.character.name}/位阶属性加成/S{self.level}"
