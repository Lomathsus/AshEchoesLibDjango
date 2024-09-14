from django.db import models
from .character import Character


class DomSkill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    description = models.TextField()
