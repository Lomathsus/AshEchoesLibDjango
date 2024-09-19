from django.db import models
from .inner_mark import InnerMark


class EtchingStats(models.Model):
    level = models.IntegerField()
    health = models.IntegerField()
    defence = models.IntegerField()
    attack = models.IntegerField()
    mastery = models.IntegerField()
    terminal = models.IntegerField()

    inner_mark = models.ForeignKey(
        InnerMark, on_delete=models.CASCADE, related_name="etching_stats"
    )

    def __str__(self):
        return f"{self.inner_mark.name}/刻印属性/Lv.{self.level}"
