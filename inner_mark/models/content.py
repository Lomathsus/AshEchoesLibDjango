from django.db import models

from inner_mark.models import InnerMark


class Content(models.Model):
    inner_mark = models.ForeignKey(
        InnerMark, on_delete=models.CASCADE, related_name="contents"
    )

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    description = models.TextField()
    detail = models.TextField()

    def __str__(self):
        return f"{self.inner_mark.name}/解锁内容/{self.name}"
