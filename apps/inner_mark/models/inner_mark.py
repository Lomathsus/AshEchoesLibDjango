from django.db import models

from constant.model_choices import RARITY_CHOICES, STAT_CHOICES
from apps.skill.models import PassiveSkill


# Create your models here.
class InnerMark(models.Model):
    name = models.CharField(max_length=50)
    rarity = models.IntegerField(choices=RARITY_CHOICES)
    stat_type = models.CharField(max_length=50, choices=STAT_CHOICES)
    illustrator = models.CharField(max_length=50, default="")
    implemented_at = models.DateField()
    acquisition = models.JSONField(default=list)
    description = models.TextField(default="")
    illustration_1 = models.TextField(default="")
    illustration_2 = models.TextField(default="")
    core_skill = models.ForeignKey(
        PassiveSkill, on_delete=models.CASCADE, related_name="inner_marks"
    )
    regular_skills = models.ManyToManyField(
        PassiveSkill,
        through="InnerMarkRegularSkill",
    )

    def save(self, *args, **kwargs):
        # Ensure that core_skill is of type 'core' or 'motivation'
        if self.core_skill.type not in ["core", "motivation"]:
            raise ValueError('Error: 核心技能类型必须是"core"或者"motivation"')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class InnerMarkRegularSkill(models.Model):
    inner_mark = models.ForeignKey(InnerMark, on_delete=models.CASCADE)
    regular_skill = models.ForeignKey(PassiveSkill, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.regular_skill.type == "regular":
            super().save(*args, **kwargs)
        else:
            raise ValueError('Error: 核心技能类型必须是"regular"')

    def __str__(self):
        return f"{self.inner_mark.name}-{self.regular_skill.name}"
