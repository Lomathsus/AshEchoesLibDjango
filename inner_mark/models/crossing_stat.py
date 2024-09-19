from django.db import models

from inner_mark.models import InnerMark


class CrossingStat(models.Model):
    inner_mark = models.ForeignKey(
        InnerMark, on_delete=models.CASCADE, related_name="crossing_stats"
    )

    name = models.CharField(max_length=100)
    unlock_level = models.IntegerField()

    def __str__(self):
        return self.name


class CrossingStatLevel(models.Model):
    crossing_stat = models.ForeignKey(
        CrossingStat, on_delete=models.CASCADE, related_name="levels"
    )
    level = models.IntegerField()
    value = models.FloatField()

    def __str__(self):
        return f"{self.crossing_stat.name}/lv{self.level}"
