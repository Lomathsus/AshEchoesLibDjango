from django.db import models
from .character import Character


class Battle(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    base_critical = models.IntegerField()
    damage_reduction = models.IntegerField()
    attack_tag = models.CharField(max_length=100)
    attack_range = models.CharField(max_length=30)
    attack_range_value = models.IntegerField()
    attack_speed = models.IntegerField()
    attack_description = models.TextField()
    movement_distance = models.IntegerField()
    movement_cooldown = models.IntegerField()
    mastery_on_heal = models.IntegerField()
    mastery_on_damage = models.IntegerField()
    mastery_on_block = models.IntegerField()
