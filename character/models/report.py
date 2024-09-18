from django.db import models
from .character import Character


class Report(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    birth_world = models.CharField(max_length=30)
    document_name = models.CharField(max_length=50)
    alias_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    faction = models.CharField(max_length=30)
    teleported_from = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=100)
    address = models.TextField()
    bref_report = models.TextField()

    def __str__(self):
        return f"Report for {self.character.name}"
