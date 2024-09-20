from django.db import models


# Create your models here.
class ActiveSkill(models.Model):
    character = models.ForeignKey(
        "character.Character", on_delete=models.CASCADE, related_name="active_skills"
    )
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50)
    tag = models.JSONField(default=list)
    cooldown_type = models.CharField(max_length=50, default="")
    cooldown = models.IntegerField(default=0)
    cast_limitation = models.IntegerField(default=-1)
    description = models.TextField(default="")
    is_seed = models.BooleanField(default=False)

    class Meta:
        db_table = "active_skill"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "name"],
                name="unique_character_active_skill",
            ),
        ]


class ActiveSkillLevel(models.Model):
    skill = models.ForeignKey(
        ActiveSkill, on_delete=models.CASCADE, related_name="levels"
    )  # 关联技能
    level = models.IntegerField()
    values = models.JSONField(default=dict)  # 使用 JSONField 存储不确定的值

    class Meta:
        db_table = "active_skill_level"
        constraints = [
            models.UniqueConstraint(
                fields=["skill", "level"],
                name="unique_skill_level",
            )
        ]

    def __str__(self):
        return f"{self.skill.name} Level {self.level}"
