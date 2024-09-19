from django.db import models
from .inner_mark import InnerMark


class Content(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, default="")
    condition = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    detail = models.TextField(default="")

    inner_mark = models.ForeignKey(
        InnerMark, on_delete=models.CASCADE, related_name="contents"
    )

    def __str__(self):
        return f"{self.inner_mark.name}/解锁内容/{self.name}"
