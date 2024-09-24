from django.db import models
from .character import Character
from common.abstract_class import BaseModel


class Equipment(BaseModel):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(default="")
    detail = models.TextField(default="")

    class Meta:
        db_table = "character_equipment"

    def __str__(self):
        return f"{self.character.name}/装备/{self.name}"
