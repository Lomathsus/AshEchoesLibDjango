from django.db import models


class PassiveSkill(models.Model):
    name = models.CharField(max_length=30)
    rarity = models.IntegerField()
    profession = models.JSONField()
    profession_type = models.JSONField()
    tag = models.JSONField()
    description = models.TextField()
    icon = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    point_requirement = models.JSONField()
    element = models.JSONField()
    skill_attribute = models.CharField(max_length=100)
    enemy_type = models.JSONField()
    activation_mode = models.JSONField()
    damage_increase = models.JSONField()
    damage_reduction = models.PositiveIntegerField()
    target_debuff = models.CharField(max_length=50)
    stat_increase = models.JSONField()
    special_mechanism = models.JSONField()

    def __str__(self):
        return self.name


class CharacterPassiveSkill(models.Model):
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    passive_skill = models.ForeignKey("PassiveSkill", on_delete=models.CASCADE)


# class MarkPassiveSkill(models.Model):
