from django.db import models
from .inner_mark import InnerMark
from apps.common.abstract_models import TimestampedModel


class EtchingStat(TimestampedModel):
    inner_mark = models.ForeignKey(
        InnerMark, on_delete=models.CASCADE, related_name="etching_stats"
    )
    level = models.IntegerField()
    health = models.IntegerField()
    defence = models.IntegerField()
    attack = models.IntegerField()
    mastery = models.IntegerField()
    terminal = models.IntegerField()

    class Meta:
        db_table = "inner_mark_etching_stat"
        constraints = [
            models.UniqueConstraint(
                fields=["inner_mark", "level"],
                name="unique_inner_mark_etching_stat",
            )
        ]

    def __str__(self):
        return f"{self.inner_mark.name}/刻印属性/Lv.{self.level}"
