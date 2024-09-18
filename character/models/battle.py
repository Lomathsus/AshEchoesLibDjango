from django.db import models
from .character import Character


class Battle(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    critical = models.IntegerField()
    damage_reduction = models.IntegerField()
    attack_name = models.CharField(max_length=30)
    attack_tag = models.JSONField()
    attack_range = models.CharField(max_length=30)
    attack_range_value = models.IntegerField()
    attack_speed = models.IntegerField()
    attack_description = models.TextField()
    movement_distance = models.IntegerField()
    movement_cooldown = models.IntegerField()
    mastery_on_heal = models.IntegerField()
    mastery_on_damage = models.IntegerField()
    mastery_on_block = models.IntegerField()
    character_enhancement = models.TextField()
