from django.db import models
from constant.model_choices import SKILL_TYPE, RARITY_CHOICES
from common.abstract_class import BaseModel


class EngravingSkill(BaseModel):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=SKILL_TYPE)
    rarity = models.IntegerField(choices=RARITY_CHOICES)
    professions = models.JSONField(default=list)
    profession_types = models.JSONField(default=list)
    tags = models.JSONField(default=list)
    description = models.TextField(default="")
    icon = models.CharField(max_length=100, default="")
    source = models.CharField(max_length=100, default="")
    point_requirement = models.JSONField(default=list)
    elements = models.JSONField(default=list)
    skill_stats = models.CharField(max_length=100, default="")
    enemy_types = models.JSONField(default=list)
    activation_modes = models.JSONField(default=list)
    damage_increases = models.JSONField(default=list)
    damage_reduction = models.IntegerField()
    target_debuffs = models.JSONField(default=list)
    stat_increases = models.JSONField(default=list)
    special_mechanism = models.JSONField(default=list)
    is_motivation = models.BooleanField(default=False)

    class Meta:
        db_table = "engraving_skill"

    def __str__(self):
        return self.name
