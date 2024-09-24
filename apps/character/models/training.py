from django.db import models

from constant.model_choices import TRAINING_CHOICES
from .character import Character
from common.abstract_class import BaseModel


class Training(BaseModel):
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


class TrainingProgram(BaseModel):
    training = models.ForeignKey(
        Training, on_delete=models.CASCADE, related_name="training_programs"
    )
    sort_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=50, choices=TRAINING_CHOICES, default="")
    value = models.IntegerField()

    class Meta:
        db_table = "character_training_program"
        constraints = [
            models.UniqueConstraint(
                fields=["training", "name"], name="unique_character_training_program"
            )
        ]

    def __str__(self):
        return f"{self.training.character.name}/{self.get_name_display()}"
