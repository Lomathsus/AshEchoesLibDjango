from django.db import models
from .character import Character
from apps.common.abstract_models import TimestampedModel


class Seed(TimestampedModel):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    init_compatibility = models.CharField(max_length=250, default="")
    bref_report = models.TextField(default="")
    cell_synchronisation_rate = models.CharField(max_length=250, default="")
    inspection_agency = models.CharField(max_length=50, default="")
    comment = models.TextField(default="")

    class Meta:
        db_table = "character_seed"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "name"], name="unique_character_seed"
            )
        ]

    def __str__(self):
        return f"{self.character.name}/异核/{self.name}"


class SeedStableCompatibility(TimestampedModel):
    seed = models.ForeignKey(
        Seed, on_delete=models.CASCADE, related_name="stable_compatibilities"
    )
    compatibility_number = models.IntegerField()
    detail = models.TextField(default="")

    class Meta:
        db_table = "character_seed_stable_compatibility"
        constraints = [
            models.UniqueConstraint(
                fields=["seed", "compatibility_number"],
                name="unique_seed_stable_compatibility",
            )
        ]

    def __str__(self):
        return f"{self.seed.character.name}/异核/相性报告{self.compatibility_number}"
