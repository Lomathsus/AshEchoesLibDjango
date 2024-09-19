from django.db import models
from .character import Character


class Battle(models.Model):
    attack_name = models.CharField(max_length=50)
    attack_tag = models.JSONField(default=list)
    attack_range = models.CharField(max_length=50)
    attack_range_value = models.IntegerField()
    attack_speed = models.IntegerField()
    attack_description = models.TextField()
    critical = models.IntegerField()
    damage_reduction = models.IntegerField()
    movement_distance = models.IntegerField()
    movement_cooldown = models.IntegerField()
    mastery_on_heal = models.IntegerField()
    mastery_on_damage = models.IntegerField()
    mastery_on_block = models.IntegerField()
    character_enhancement = models.TextField(default="")

    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.character.name}/战斗属性"
