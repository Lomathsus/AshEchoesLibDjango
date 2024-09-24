from . import (
    ActiveManager,
    SoftDeletionModel,
    SoftDeletionManager,
    TimestampModel,
    TimestampManager,
)


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


__all__ = ["BaseModel"]
