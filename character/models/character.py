from django.db import models

from skill.models import PassiveSkill


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=30, null=False)
    en_name = models.CharField(max_length=30)
    jp_name = models.CharField(max_length=30)
    cn_cv = models.CharField(max_length=30)
    jp_cv = models.CharField(max_length=30)
    profession = models.CharField(max_length=30, null=False)
    element = models.CharField(max_length=30, null=False)
    rarity = models.IntegerField(null=False)
    tag = models.JSONField()
    prototype = models.CharField(max_length=30)
    implemented_at = models.DateField(null=False)
    acquisition = models.JSONField()
    music_name = models.CharField(max_length=50)
    expression = models.JSONField()
    passive_skills = models.ManyToManyField(
        PassiveSkill, through="CharacterPassiveSkill"
    )

    def __str__(self):
        return self.name


class CharacterPassiveSkill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    passive_skill = models.ForeignKey(PassiveSkill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.character.name}-{self.passive_skill.name}"
