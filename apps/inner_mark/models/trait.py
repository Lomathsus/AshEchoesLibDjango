from django.db import models

from .inner_mark import InnerMark
from apps.common.abstract_models import TimestampedModel


class Trait(TimestampedModel):
    inner_mark = models.ForeignKey(
        InnerMark, on_delete=models.CASCADE, related_name="traits"
    )
    description = models.TextField(default="")
    level_max_addition = models.TextField(default="")

    class Meta:
        db_table = "inner_mark_trait"

    def __str__(self):
        return f"{self.inner_mark.name}/特质"


class TraitLevel(TimestampedModel):
    trait = models.ForeignKey(Trait, on_delete=models.CASCADE, related_name="levels")
    level = models.IntegerField()
    values = models.JSONField()

    class Meta:
        db_table = "inner_mark_trait_level"

    def __str__(self):
        return f"{self.trait.inner_mark.name}/特质/Lv.{self.level}"
