from django.db import models
from .character import Character


class Report(models.Model):
    gender = models.CharField(max_length=50)
    height = models.IntegerField(default=-1)
    birthday = models.CharField(max_length=50, default="")
    document_name = models.CharField(max_length=50, default="")
    birth_world = models.CharField(max_length=50, default="")
    alias_name = models.CharField(max_length=50, default="")
    faction = models.CharField(max_length=50, default="")
    teleported_from = models.CharField(max_length=100, default="")
    birthplace = models.CharField(max_length=100, default="")
    address = models.TextField(default="")
    bref_report = models.TextField(default="")

    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.character.name}/个人报告"
