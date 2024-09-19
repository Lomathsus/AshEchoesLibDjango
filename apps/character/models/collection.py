from django.db import models
from .character import Character


class Collection(models.Model):
    sort_number = models.IntegerField()
    description = models.TextField(default="")

    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="collections"
    )

    def __str__(self):
        return f"{self.character.name}/收藏/{self.sort_number}"
