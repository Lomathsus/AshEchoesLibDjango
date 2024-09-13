from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=30, null=False)
    en_name = models.CharField(max_length=30)
    jp_name = models.CharField(max_length=30)
    cn_cv =  models.CharField(max_length=30)
    jp_cv =  models.CharField(max_length=30)
    profession = models.CharField(max_length=30, null=False)
    element= models.CharField(max_length=30, null=False)
    rarity = models.IntegerField(null=False)
    tag = models.CharField(max_length=100)
    prototype =  models.CharField(max_length=30)
    implemented_at = models.DateField(null=False)
    acquisition = models.CharField(max_length=100)
    music_name = models.CharField(max_length=50)
    expression = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Report(models.Model):
    character= models.OneToOneField(Character, on_delete=models.CASCADE)

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

class Seed(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    init_compatibility= models.CharField(max_length=250)
    bref_report = models.TextField()
    stable_compatibility_1 = models.CharField(max_length=100)
    stable_compatibility_2 = models.CharField(max_length=100)
    stable_compatibility_3 = models.CharField(max_length=100)
    cell_synchronisation_rate = models.CharField(max_length=100)
    inspection_agency = models.CharField(max_length=50)
    comment = models.TextField()

    def __str__(self):
        return f"Seed for {self.character.name}"

class DomSkill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    description = models.TextField()


class Training(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    step = models.IntegerField()
