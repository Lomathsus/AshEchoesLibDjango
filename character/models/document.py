from django.db import models
from .character import Character


class Document(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="documents"
    )

    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
