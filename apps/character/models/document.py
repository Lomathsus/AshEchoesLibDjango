from django.db import models
from .character import Character


class Document(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="documents"
    )
    name = models.CharField(max_length=100)
    content = models.TextField(default="")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "name"], name="unique_character_document"
            )
        ]

    def __str__(self):
        return f"{self.character.name}/档案/{self.name}"
