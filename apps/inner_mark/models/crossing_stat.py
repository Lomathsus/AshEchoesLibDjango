from django.db import models
from .inner_mark import InnerMark


class CrossingStat(models.Model):
    name = models.CharField(max_length=100)
    unlock_level = models.IntegerField(default=-1)

    inner_mark = models.ForeignKey(
        InnerMark, on_delete=models.CASCADE, related_name="crossing_stats"
    )

    def __str__(self):
        return self.name


class CrossingStatLevel(models.Model):
    level = models.IntegerField()
    value = models.FloatField()

    crossing_stat = models.ForeignKey(
        CrossingStat, on_delete=models.CASCADE, related_name="levels"
    )

    def __str__(self):
        return f"{self.crossing_stat.name}/lv{self.level}"
