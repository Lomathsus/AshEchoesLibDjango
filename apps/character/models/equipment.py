from django.db import models
from .character import Character


class Equipment(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(default="")
    detail = models.TextField(default="")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "name"], name="unique_character_equipment"
            )
        ]

    def __str__(self):
        return f"{self.character.name}/装备/{self.name}"
