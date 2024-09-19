from django.db import models
from .character import Character


class DomSkill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="")

    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="dom_skills"
    )

    def __str__(self):
        return f"{self.character.name}/穹顶技能/{self.name}"
