from django.db import models

from constant.model_choices import STAT_CHOICES
from .memory_trace import MemoryTrace
from common.abstract_class import BaseModel


class Awaking(BaseModel):
    AWAKING_CHOICES = STAT_CHOICES + [
        ("skill_point", "技能点"),
    ]

    memory_trace = models.ForeignKey(
        MemoryTrace, on_delete=models.CASCADE, related_name="awakings"
    )
    phase_number = models.IntegerField()
    choice_number = models.IntegerField()
    name = models.CharField(max_length=50, choices=AWAKING_CHOICES)
    values = models.JSONField(default=list)

    class Meta:
        db_table = "memory_trace_awaking"
        constraints = [
            models.UniqueConstraint(
                fields=["memory_trace", "phase_number", "choice_number"],
                name="unique_awaking",
            )
        ]

    def __str__(self):
        return f"{self.memory_trace.name}/唤醒/阶段{self.phase_number}/选项{self.choice_number}/{self.get_name_display()}"
