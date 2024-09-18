from django.db import models
from .character import Character


class Equipment(models.Model):
    character = models.OneToOneField(
        Character, on_delete=models.CASCADE, related_name="equipment"
    )

    name = models.CharField(max_length=30)
    description = models.TextField()
    detail = models.TextField()

    def __str__(self):
        return self.name
