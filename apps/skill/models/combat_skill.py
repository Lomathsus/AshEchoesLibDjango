from django.db import models
from common.abstract_class import BaseModel


# Create your models here.
class CombatSkill(BaseModel):
    character = models.ForeignKey(
        "character.Character", on_delete=models.CASCADE, related_name="combat_skills"
    )
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50)
    tags = models.JSONField(default=list)
    cooldown_type = models.CharField(max_length=50, default="")
    cooldown = models.IntegerField(default=0)
    availability = models.IntegerField(default=-1)
    description = models.TextField(default="")
    cast_condition = models.TextField(default="")
    cast_duration = models.IntegerField(default=-1)
    is_seed = models.BooleanField(default=False)

    class Meta:
        db_table = "combat_skill"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "name"],
                name="unique_character_combat_skill",
            ),
        ]


class CombatSkillLevel(BaseModel):
    combat_skill = models.ForeignKey(
        CombatSkill, on_delete=models.CASCADE, related_name="levels"
    )  # 关联技能
    level = models.IntegerField()
    values = models.JSONField(default=dict)  # 使用 JSONField 存储不确定的值

    class Meta:
        db_table = "combat_skill_level"
        constraints = [
            models.UniqueConstraint(
                fields=["combat_skill", "level"],
                name="unique_combat_skill_level",
            )
        ]

    def __str__(self):
        return f"{self.combat_skill.name} Level {self.level}"
