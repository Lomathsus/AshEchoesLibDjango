from django.db import models
from .character import Character


class Collection(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="collections"
    )
    collection_number = models.IntegerField()
    description = models.TextField(default="")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "collection_number"],
                name="unique_character_collection",
            )
        ]

    def __str__(self):
        return f"{self.character.name}/收藏/{self.sort_number}"
