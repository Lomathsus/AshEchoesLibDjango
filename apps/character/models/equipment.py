from django.db import models
from .character import Character


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="")
    detail = models.TextField(default="")

    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.character.name}/装备/{self.name}"
