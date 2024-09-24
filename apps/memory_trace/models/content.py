from django.db import models
from .memory_trace import MemoryTrace
from common.abstract_class import BaseModel


class Content(BaseModel):
    memory_trace = models.ForeignKey(
        MemoryTrace, on_delete=models.CASCADE, related_name="contents"
    )
    sort_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, default="")
    condition = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    detail = models.TextField(default="")

    class Meta:
        db_table = "memory_trace_content"

    def __str__(self):
        return f"{self.memory_trace.name}/解锁内容/{self.name}"
