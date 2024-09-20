from django.db import models
from constant.model_choices import SKILL_TYPE


class PassiveSkill(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=SKILL_TYPE)
    rarity = models.IntegerField()
    profession = models.JSONField(default=list)
    profession_type = models.JSONField(default=list)
    tag = models.JSONField(default=list)
    description = models.TextField(default="")
    icon = models.CharField(max_length=100, default="")
    source = models.CharField(max_length=100, default="")
    point_requirement = models.JSONField(default=list)
    element = models.JSONField(default=list)
    skill_attribute = models.CharField(max_length=100, default="")
    enemy_type = models.JSONField(default=list)
    activation_mode = models.JSONField(default=list)
    damage_increase = models.JSONField(default=list)
    damage_reduction = models.IntegerField()
    target_debuff = models.JSONField(default=list)
    stat_increase = models.JSONField(default=list)
    special_mechanism = models.JSONField(default=list)

    class Meta:
        db_table = "passive_skill"

    def __str__(self):
        return self.name
