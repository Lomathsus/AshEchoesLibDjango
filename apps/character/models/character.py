from django.db import models

from apps.skill.models import PassiveSkill
from apps.common.abstract_models import TimestampedModel


# Create your models here.
class Character(TimestampedModel):
    name = models.CharField(max_length=50)
    en_name = models.CharField(max_length=50, default="")
    jp_name = models.CharField(max_length=50, default="")
    cn_cv = models.CharField(max_length=50, default="")
    jp_cv = models.CharField(max_length=50, default="")
    profession = models.CharField(max_length=50)
    element = models.CharField(max_length=50)
    rarity = models.IntegerField()
    tag = models.JSONField(default=list)
    prototype = models.CharField(max_length=50)
    implemented_at = models.DateField()
    acquisition = models.JSONField(default=list)
    music_name = models.CharField(max_length=50, default="")
    expression = models.JSONField(default=list)
    passive_skills = models.ManyToManyField(
        PassiveSkill, through="CharacterPassiveSkill"
    )

    class Meta:
        db_table = "character_info"

    def __str__(self):
        return self.name


class CharacterPassiveSkill(TimestampedModel):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    passive_skill = models.ForeignKey(PassiveSkill, on_delete=models.CASCADE)

    class Meta:
        db_table = "character_passive_skill_relationship"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "passive_skill"],
                name="unique_character_passive_skill",
            )
        ]

    def __str__(self):
        return f"{self.character.name}/{self.passive_skill.name}"
