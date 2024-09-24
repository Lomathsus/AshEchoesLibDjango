from django.db import models
from .character import Character
from common.abstract_class import BaseModel


class Document(BaseModel):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="documents"
    )
    name = models.CharField(max_length=100)
    content = models.TextField(default="")

    class Meta:
        db_table = "character_document"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "name"], name="unique_character_document"
            )
        ]

    def __str__(self):
        return f"{self.character.name}/档案/{self.name}"
