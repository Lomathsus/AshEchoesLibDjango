from django.db import models
from .inner_mark import InnerMark
from apps.common.abstract_models import TimestampedModel


class Awaken(TimestampedModel):
    NAME_CHOICES = [
        ("health", "体质"),
        ("defence", "防御"),
        ("attack", "攻击"),
        ("mastery", "专精"),
        ("terminal", "终端"),
        ("skill_point", "技能点"),
    ]

    inner_mark = models.ForeignKey(
        InnerMark, on_delete=models.CASCADE, related_name="awakens"
    )
    phase_number = models.IntegerField()
    choice_number = models.IntegerField()
    name = models.CharField(max_length=50, choices=NAME_CHOICES)
    value = models.JSONField(default=list)

    class Meta:
        db_table = "inner_mark_awaken"
        constraints = [
            models.UniqueConstraint(
                fields=["inner_mark", "phase_number", "choice_number"],
                name="unique_awaken",
            )
        ]

    def __str__(self):
        return f"{self.inner_mark.name}/唤醒/阶段{self.phase_number}/选项{self.choice_number}/{self.get_name_display()}"
