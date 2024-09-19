from django.db import models


# Create your models here.
class CharacterSkill(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    tag = models.JSONField(default=list)
    cooldown_type = models.CharField(max_length=50, default="")
    cooldown = models.IntegerField(default=0)
    cast_limitation = models.IntegerField(default=-1)
    description = models.TextField(default="")
    is_seed = models.BooleanField(default=False)

    character = models.ForeignKey(
        "character.Character", on_delete=models.CASCADE, related_name="character_skills"
    )


class CharacterSkillLevel(models.Model):
    level = models.IntegerField()
    values = models.JSONField(default=dict)  # 使用 JSONField 存储不确定的值

    skill = models.ForeignKey(
        CharacterSkill, on_delete=models.CASCADE, related_name="levels"
    )  # 关联技能

    def __str__(self):
        return f"{self.skill.name} Level {self.level}"
