from django.db import models
from .character import Character


class TrainingAttribute(models.Model):
    # 定义所有可能的训练属性
    attribute_choices = [
        ("health", "体质"),
        ("defence", "防御"),
        ("attack", "攻击"),
        ("mastery", "专精"),
        ("terminal", "终端"),
        ("attack_speed", "攻击速度"),
        ("heal", "治愈力"),
        ("block", "格挡强度"),
        ("damage_reduction", "减伤"),
    ]

    attribute = models.CharField(max_length=20, choices=attribute_choices)

    value = models.IntegerField()  # 可根据具体需求选择合适的数据类型

    def __str__(self):
        return f"{self.get_attribute_display()}: {self.value}"


class Training(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)

    # 阶段1的训练属性
    phase1_attribute1 = models.ForeignKey(
        TrainingAttribute, related_name="phase1_attr1", on_delete=models.CASCADE
    )
    phase1_attribute2 = models.ForeignKey(
        TrainingAttribute, related_name="phase1_attr2", on_delete=models.CASCADE
    )
    phase1_attribute3 = models.ForeignKey(
        TrainingAttribute, related_name="phase1_attr3", on_delete=models.CASCADE
    )

    # 阶段2的训练属性
    phase2_attribute1 = models.ForeignKey(
        TrainingAttribute, related_name="phase2_attr1", on_delete=models.CASCADE
    )
    phase2_attribute2 = models.ForeignKey(
        TrainingAttribute, related_name="phase2_attr2", on_delete=models.CASCADE
    )
    phase2_attribute3 = models.ForeignKey(
        TrainingAttribute, related_name="phase2_attr3", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
