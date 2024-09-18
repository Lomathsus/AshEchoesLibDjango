from django.db import models

from .inner_mark import InnerMark


class Trait(models.Model):
    inner_mark = models.ForeignKey(InnerMark, on_delete=models.CASCADE)
    description = models.TextField()
    level_max_addition = models.TextField()

    def __str__(self):
        return f"{self.inner_mark.name}/特质"


class TraitLevel(models.Model):
    trait = models.ForeignKey(Trait, on_delete=models.CASCADE)

    level = models.IntegerField()
    values = models.JSONField()

    def __str__(self):
        return f"{self.trait.inner_mark.name}/特质/lv{self.level}"
