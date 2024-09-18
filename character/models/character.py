from django.db import models


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=30, null=False)
    en_name = models.CharField(max_length=30)
    jp_name = models.CharField(max_length=30)
    cn_cv = models.CharField(max_length=30)
    jp_cv = models.CharField(max_length=30)
    profession = models.CharField(max_length=30, null=False)
    element = models.CharField(max_length=30, null=False)
    rarity = models.IntegerField(null=False)
    tag = models.JSONField()
    prototype = models.CharField(max_length=30)
    implemented_at = models.DateField(null=False)
    acquisition = models.JSONField()
    music_name = models.CharField(max_length=50)
    expression = models.JSONField()

    def __str__(self):
        return self.name
