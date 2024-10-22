from django.utils import timezone

from utils.extract_number import extract_number
from . import (
    ActiveManager,
    SoftDeletionModel,
    SoftDeletionManager,
    TimestampModel,
    TimestampManager,
)
from django.db import models


class DeletedCombineManger(SoftDeletionManager, TimestampManager):
    pass


class ActiveCombineManger(ActiveManager, TimestampManager):
    pass


class BaseModel(SoftDeletionModel, TimestampModel):
    # 设置自定义管理器
    objects = TimestampManager()
    deleted = DeletedCombineManger()
    active = ActiveCombineManger()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        for field in self._meta.fields:
            value = getattr(self, field.name, None)
            if isinstance(value, str):
                if isinstance(field, models.IntegerField):
                    try:
                        setattr(self, field.name, extract_number(value))
                    except ValueError:
                        setattr(self, field.name, 0)
                elif isinstance(field, models.FloatField):
                    try:
                        setattr(self, field.name, extract_number(value))
                    except ValueError:
                        setattr(self, field.name, 0.0)

            # 检查是否是新创建的实例或者有字段发生变化
        if self.pk is not None:
            original = type(self).objects.get(pk=self.pk)
            has_changed = any(
                getattr(self, field.name) != getattr(original, field.name)
                for field in self._meta.fields
                if field.name != "updated_at"
            )
        else:
            has_changed = True  # 新创建的实例认为数据发生了变化

            # 如果有变化，更新 updated_at 字段并保存
        if has_changed:
            self.updated_at = timezone.now()
        else:
            kwargs["update_fields"] = [
                field.name
                for field in self._meta.fields
                if not field.auto_created and field.name != "updated_at"
            ]
        super().save(*args, **kwargs)


__all__ = ["BaseModel"]
