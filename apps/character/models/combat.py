from django.db import models
from .character import Character
from common.abstract_class import BaseModel


class Combat(BaseModel):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    attack_tags = models.JSONField(default=list)
    attack_range = models.CharField(max_length=50)
    attack_range_value = models.IntegerField()
    attack_speed = models.IntegerField()
    attack_description = models.TextField()
    critical_rate = models.IntegerField()
    basic_damage_reduction = models.IntegerField()
    reposition_distance = models.IntegerField()
    reposition_cooldown = models.IntegerField()
    mastery_on_heal = models.IntegerField()
    mastery_on_damage = models.IntegerField()
    mastery_on_block = models.IntegerField()
    character_enhancement = models.TextField(default="")

    class Meta:
        db_table = "character_combat"

    def __str__(self):
        return f"{self.character.name}/战斗属性"
