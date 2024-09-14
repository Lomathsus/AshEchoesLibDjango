from django.db import models
from .character import Character


class Seed(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    init_compatibility = models.CharField(max_length=250)
    bref_report = models.TextField()
    stable_compatibility_1 = models.CharField(max_length=100)
    stable_compatibility_2 = models.CharField(max_length=100)
    stable_compatibility_3 = models.CharField(max_length=100)
    cell_synchronisation_rate = models.CharField(max_length=100)
    inspection_agency = models.CharField(max_length=50)
    comment = models.TextField()

    def __str__(self):
        return f"Seed for {self.character.name}"
