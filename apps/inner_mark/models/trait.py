from django.db import models

from .inner_mark import InnerMark


class Trait(models.Model):
    description = models.TextField(default="")
    level_max_addition = models.TextField(default="")

    inner_mark = models.ForeignKey(
        InnerMark, on_delete=models.CASCADE, related_name="traits"
    )

    def __str__(self):
        return f"{self.inner_mark.name}/特质"


class TraitLevel(models.Model):
    level = models.IntegerField()
    values = models.JSONField()

    trait = models.ForeignKey(Trait, on_delete=models.CASCADE, related_name="levels")

    def __str__(self):
        return f"{self.trait.inner_mark.name}/特质/Lv.{self.level}"
