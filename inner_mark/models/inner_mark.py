from django.db import models

from constant.model_choices import RARITY_CHOICES, STAT_CHOICES
from skill.models import PassiveSkill


# Create your models here.
class InnerMark(models.Model):
    name = models.CharField(max_length=50)
    rarity = models.IntegerField(choices=RARITY_CHOICES)
    stat = models.CharField(max_length=50, choices=STAT_CHOICES)
    illustrator = models.CharField(max_length=50)
    implemented_at = models.DateField()
    acquisition = models.JSONField()
    description = models.TextField()
    illustration_1 = models.TextField()
    illustration_2 = models.TextField()
    skills = models.ManyToManyField(PassiveSkill, through="InnerMarkPassiveSkill")

    def __str__(self):
        return self.name


class InnerMarkPassiveSkill(models.Model):
    inner_mark = models.ForeignKey(InnerMark, on_delete=models.CASCADE)
    passive_skill = models.ForeignKey(PassiveSkill, on_delete=models.CASCADE)
    is_mark_skill = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.inner_mark.name}-{self.passive_skill.name}"
