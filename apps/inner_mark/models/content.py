from django.db import models
from .inner_mark import InnerMark
from apps.common.abstract_models import TimestampedModel


class Content(TimestampedModel):
    inner_mark = models.ForeignKey(
        InnerMark, on_delete=models.CASCADE, related_name="contents"
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, default="")
    condition = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    detail = models.TextField(default="")

    class Meta:
        db_table = "inner_mark_content"

    def __str__(self):
        return f"{self.inner_mark.name}/解锁内容/{self.name}"
