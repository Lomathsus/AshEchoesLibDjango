from django.db import models
from constant.model_choices import RARITY_CHOICES, STAT_CHOICES
from apps.skill.models import EngravingSkill
from common.abstract_class import BaseModel


# Create your models here.
class MemoryTrace(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    rarity = models.IntegerField(choices=RARITY_CHOICES)
    type = models.CharField(max_length=50, choices=STAT_CHOICES)
    artist = models.CharField(max_length=50, default="")
    implemented_at = models.IntegerField(null=True, blank=True)
    acquisitions = models.JSONField(default=list)
    description = models.TextField(default="")
    illustration_1 = models.TextField(default="")
    illustration_2 = models.TextField(default="")
    engraving_skills = models.ManyToManyField(
        EngravingSkill,
        through="MemoryTraceEngravingSkill",
    )

    class Meta:
        db_table = "inner_mark_info"

    def __str__(self):
        return self.name


class MemoryTraceEngravingSkill(BaseModel):
    memory_trace = models.ForeignKey(MemoryTrace, on_delete=models.CASCADE)
    engraving_skill = models.ForeignKey(EngravingSkill, on_delete=models.CASCADE)

    class Meta:
        db_table = "memory_trace_engraving_skill_relationship"
        constraints = [
            models.UniqueConstraint(
                fields=["memory_trace", "engraving_skill"],
                name="unique_memory_trace_engraving_skill",
            )
        ]

    def __str__(self):
        return f"{self.memory_trace.name}/{self.engraving_skill.get_type_display()}/{self.engraving_skill.name}"
