from django.db import models, IntegrityError

from apps.skill.models import EngravingSkill
from common.abstract_class import BaseModel
from constant.model_choices import RARITY_CHOICES


# Create your models here.
class Character(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    en_name = models.CharField(max_length=50, default="")
    jp_name = models.CharField(max_length=50, default="")
    cn_cv = models.CharField(max_length=50, default="")
    jp_cv = models.CharField(max_length=50, default="")
    profession = models.CharField(max_length=50)
    element = models.CharField(max_length=50)
    rarity = models.IntegerField(choices=RARITY_CHOICES)
    tags = models.JSONField(default=list)
    prototype = models.CharField(max_length=50)
    implemented_at = models.IntegerField(null=True, blank=True)
    acquisitions = models.JSONField(default=list)
    music_name = models.CharField(max_length=50, default="")
    expressions = models.JSONField(default=list)
    engraving_skills = models.ManyToManyField(
        EngravingSkill, through="CharacterEngravingSkill"
    )

    class Meta:
        db_table = "character_info"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)

        except IntegrityError as e:
            if "unique_field" in str(e):
                # 当unique字段冲突时，查询并返回已存在的那条数据
                existing_object = Character.objects.get(unique_field=self.name)
                return existing_object
            else:
                return None


class CharacterEngravingSkill(BaseModel):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    engraving_skill = models.ForeignKey(EngravingSkill, on_delete=models.CASCADE)

    class Meta:
        db_table = "character_engraving_skill_relationship"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "engraving_skill"],
                name="unique_character_engraving_skill",
            )
        ]

    def __str__(self):
        return f"{self.character.name}/刻印技能/{self.engraving_skill.name}"
