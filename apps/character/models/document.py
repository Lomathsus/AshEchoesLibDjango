from django.db import models
from .character import Character


class Document(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default="")

    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="documents"
    )

    def __str__(self):
        return f"{self.character.name}/档案/{self.name}"
