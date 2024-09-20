from django.db import models
from .character import Character
from apps.common.abstract_models import TimestampedModel


class Training(TimestampedModel):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="trainings"
    )
    phase = models.IntegerField()

    class Meta:
        db_table = "character_training"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "phase"], name="unique_character_training_phase"
            )
        ]

    def __str__(self):
        return f"{self.character.name}/穹顶训练 - Phase {self.phase}"


class TrainingProgram(TimestampedModel):
    STAT_CHOICES = [
        ("health", "体质"),
        ("defence", "防御"),
        ("attack", "攻击"),
        ("mastery", "专精"),
        ("terminal", "终端"),
        ("attack_speed", "攻击速度"),
        ("heal", "治愈力"),
        ("block", "格挡强度"),
        ("damage_reduction", "减伤"),
    ]
    training = models.ForeignKey(
        Training, on_delete=models.CASCADE, related_name="training_programs"
    )
    name = models.CharField(max_length=20, choices=STAT_CHOICES, default="")
    value = models.IntegerField()  # 可根据具体需求选择合适的数据类型
    sort_number = models.IntegerField()

    class Meta:
        db_table = "character_training_program"
        constraints = [
            models.UniqueConstraint(
                fields=["training", "name"], name="unique_character_training_program"
            )
        ]

    def __str__(self):
        return f"{self.training.character.name}/{self.get_name_display()}"
