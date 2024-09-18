from django.db import models

from character.models import Character


# Create your models here.
class CharacterSkill(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="skills"
    )

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    tag = models.CharField(max_length=100)
    cooldown_type = models.CharField(max_length=30)
    cooldown = models.IntegerField()
    cast_limitation = models.IntegerField()
    description = models.TextField()
    is_seed = models.BooleanField(default=False)


class CharacterSkillLevel(models.Model):
    skill = models.ForeignKey(
        CharacterSkill, on_delete=models.CASCADE, related_name="levels"
    )  # 关联技能

    level = models.IntegerField()
    values = models.JSONField()  # 使用 JSONField 存储不确定的值

    def __str__(self):
        return f"{self.skill.name} Level {self.level}"
