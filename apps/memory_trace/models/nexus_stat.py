from django.db import models
from .memory_trace import MemoryTrace
from common.abstract_class import BaseModel


class NexusStat(BaseModel):
    memory_trace = models.ForeignKey(
        MemoryTrace, on_delete=models.CASCADE, related_name="nexus_stats"
    )
    name = models.CharField(max_length=100)
    unlock_level = models.IntegerField(default=-1)

    class Meta:
        db_table = "memory_trace_nexus_stat"

    def __str__(self):
        return self.name


class NexusStatLevel(BaseModel):
    nexus_stat = models.ForeignKey(
        NexusStat, on_delete=models.CASCADE, related_name="levels"
    )
    level = models.IntegerField()
    value = models.FloatField()

    class Meta:
        db_table = "memory_trace_nexus_stat_level"
        constraints = [
            models.UniqueConstraint(
                fields=["nexus_stat", "level"], name="unique_nexus_stat_level"
            )
        ]

    def __str__(self):
        return f"{self.nexus_stat.name}/lv{self.level}"
