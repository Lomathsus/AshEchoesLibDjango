from django.db import models

from .inner_mark import InnerMark


class Awaken(models.Model):
    inner_mark = models.ForeignKey(
        InnerMark, on_delete=models.CASCADE, related_name="awakens"
    )

    phase_number = models.IntegerField()
    choice_number = models.IntegerField()
    value_type = models.CharField(max_length=50)
    value = models.JSONField()
