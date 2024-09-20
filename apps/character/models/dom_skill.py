from django.db import models
from .character import Character
from apps.common.abstract_models import TimestampedModel


class DomSkill(TimestampedModel):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="dom_skills"
    )
    name = models.CharField(max_length=50)
    description = models.TextField(default="")

    class Meta:
        db_table = "character_dom_skill"
        constraints = [
            models.UniqueConstraint(
                fields=["character", "name"], name="unique_character_dom_skill"
            )
        ]

    def __str__(self):
        return f"{self.character.name}/穹顶技能/{self.name}"
