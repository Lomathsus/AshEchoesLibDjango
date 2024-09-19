from django.db import models
from .character import Character


class Seed(models.Model):
    name = models.CharField(max_length=50)
    init_compatibility = models.CharField(max_length=250, default="")
    bref_report = models.TextField(default="")
    stable_compatibility_1 = models.CharField(max_length=250, default="")
    stable_compatibility_2 = models.CharField(max_length=250, default="")
    stable_compatibility_3 = models.CharField(max_length=250, default="")
    cell_synchronisation_rate = models.CharField(max_length=250, default="")
    inspection_agency = models.CharField(max_length=50, default="")
    comment = models.TextField(default="")

    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.character.name}/异核/{self.name}"
