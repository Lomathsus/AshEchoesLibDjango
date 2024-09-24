from django.db import models
from django.utils import timezone
from datetime import timedelta


class TimestampManager(models.Manager):
    def recent(self, days=1):
        """获取最近days天内创建的记录"""
        now = timezone.now()
        return self.filter(created_at__gte=now - timedelta(days=days))

    def recently_updated(self, days=1):
        """获取最近days天内更新的记录"""
        now = timezone.now()
        return self.filter(updated_at__gte=now - timedelta(days=days))

    def created_between(self, start_date, end_date):
        """获取在 start_date 和 end_date 之间创建的记录"""
        return self.filter(created_at__gte=start_date, created_at__lte=end_date)

    def updated_between(self, start_date, end_date):
        """获取在 start_date 和 end_date 之间更新的记录"""
        return self.filter(updated_at__gte=start_date, updated_at__lte=end_date)


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True
