from django.db import models
from .character import Character


class Collection(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="collections"
    )

    item_number = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"item_{self.item_number}"
