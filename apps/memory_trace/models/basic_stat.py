from django.db import models
from .memory_trace import MemoryTrace
from common.abstract_class import BaseModel


class BasicStat(BaseModel):
    memory_trace = models.ForeignKey(
        MemoryTrace, on_delete=models.CASCADE, related_name="basic_stats"
    )
    level = models.IntegerField()
    vitality = models.IntegerField()
    defence = models.IntegerField()
    attack = models.IntegerField()
    mastery = models.IntegerField()
    terminal = models.IntegerField()

    class Meta:
        db_table = "memory_trace_basic_stat"
        constraints = [
            models.UniqueConstraint(
                fields=["memory_trace", "level"],
                name="unique_memory_trace_basic_stat",
            )
        ]

    def __str__(self):
        return f"{self.memory_trace.name}/刻印属性/Lv.{self.level}"
