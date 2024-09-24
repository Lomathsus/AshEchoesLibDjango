from django.db import models

from .memory_trace import MemoryTrace
from common.abstract_class import BaseModel


class NexusEffect(BaseModel):
    memory_trace = models.ForeignKey(
        MemoryTrace, on_delete=models.CASCADE, related_name="nexus_effects"
    )
    description = models.TextField(default="")
    level_max_addition = models.TextField(default="")

    class Meta:
        db_table = "memory_trace_nexus_effect"

    def __str__(self):
        return f"{self.memory_trace.name}/特质"


class NexusEffectLevel(BaseModel):
    nexus_effect = models.ForeignKey(
        NexusEffect, on_delete=models.CASCADE, related_name="levels"
    )
    level = models.IntegerField()
    values = models.JSONField()

    class Meta:
        db_table = "memory_trace_nexus_effect_level"

    def __str__(self):
        return f"{self.nexus_effect.memory_trace.name}/特质/Lv.{self.level}"
