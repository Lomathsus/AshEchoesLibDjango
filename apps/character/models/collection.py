from django.db import models
from .character import Character
from common.abstract_class import BaseModel


class Collection(BaseModel):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="collections"
    )
    sort_number = models.IntegerField(unique=True)
    description = models.TextField(default="")

    class Meta:
        db_table = "character_collection"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "sort_number"],
                name="unique_character_collection",
            )
        ]

    def __str__(self):
        return f"{self.character.name}/收藏/{self.sort_number}"
