from django.db import models
from django.utils import timezone
from datetime import timedelta, datetime
from django.utils.timesince import timeuntil


class TimestampManager(models.Manager):
    def recent(self, days=1):
        """获取最近days天内创建的记录"""
        now_timestamp = timezone.now().timestamp()
        time_threshold = now_timestamp - timedelta(days=days).total_seconds()
        return self.filter(created_at__gte=time_threshold)

    def recently_updated(self, days=1):
        """获取最近days天内更新的记录"""
        now_timestamp = timezone.now().timestamp()
        time_threshold = now_timestamp - timedelta(days=days).total_seconds()
        return self.filter(updated_at__gte=time_threshold)

    def created_between(self, start_date, end_date):
        """获取在 start_date 和 end_date 之间创建的记录"""
        start_timestamp = start_date.timestamp()
        end_timestamp = end_date.timestamp()
        return self.filter(
            created_at__gte=start_timestamp, created_at__lte=end_timestamp
        )

    def updated_between(self, start_date, end_date):
        """获取在 start_date 和 end_date 之间更新的记录"""
        start_timestamp = start_date.timestamp()
        end_timestamp = end_date.timestamp()
        return self.filter(
            updated_at__gte=start_timestamp, updated_at__lte=end_timestamp
        )


class TimestampModel(models.Model):
    created_at = models.IntegerField()
    updated_at = models.IntegerField(blank=True, null=True)

    objects = TimestampManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:  # 使用pk属性来处理自定义主键字段
            self.created_at = timezone.now().timestamp()
        self.updated_at = timezone.now().timestamp()
        super().save(*args, **kwargs)
