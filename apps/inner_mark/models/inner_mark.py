from django.db import models

from constant.model_choices import RARITY_CHOICES, STAT_CHOICES
from apps.skill.models import PassiveSkill


# Create your models here.
class InnerMark(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rarity = models.IntegerField(choices=RARITY_CHOICES)
    stat_type = models.CharField(max_length=50, choices=STAT_CHOICES)
    illustrator = models.CharField(max_length=50, default="")
    implemented_at = models.DateField()
    acquisition = models.JSONField(default=list)
    description = models.TextField(default="")
    illustration_1 = models.TextField(default="")
    illustration_2 = models.TextField(default="")
    passive_skills = models.ManyToManyField(
        PassiveSkill,
        through="InnerMarkPassiveSkill",
    )

    class Meta:
        db_table = "inner_mark"

    def __str__(self):
        return self.name


class InnerMarkPassiveSkill(models.Model):
    inner_mark = models.ForeignKey(InnerMark, on_delete=models.CASCADE)
    passive_skill = models.ForeignKey(PassiveSkill, on_delete=models.CASCADE)

    class Meta:
        db_table = "inner_mark_passive_skill"
        constraints = [
            models.UniqueConstraint(
                fields=["inner_mark", "passive_skill"],
                name="unique_inner_mark_passive_skill",
            )
        ]

    def __str__(self):
        return f"{self.inner_mark.name}/{self.passive_skill.get_type_display()}/{self.passive_skill.name}"
