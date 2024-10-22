from django.db import models

from apps.character.models import Character
from common.abstract_class import BaseModel


class Trait(BaseModel):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "character_trait"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "name"], name="unique_character_trait"
            )
        ]

    def __str__(self):
        return f"{self.character.name}/特性 - {self.name}"


class TraitLevel(BaseModel):
    trait = models.ForeignKey(
        Trait, on_delete=models.CASCADE, related_name="trait_levels"
    )
    level = models.IntegerField()
    description = models.TextField(default="")

    class Meta:
        db_table = "character_trait_level"
        constraints = [
            models.UniqueConstraint(
                fields=["trait", "level"], name="unique_trait_level"
            )
        ]

    def __str__(self):
        return f"{self.trait.character.name}/特性 - level {self.level}"
