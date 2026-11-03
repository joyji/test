"""SLA 截止时间计算。"""

from datetime import timedelta

from .priority import sla_hours


def due_at(created_at, priority):
    """返回工单的 SLA 截止时间。"""
    return created_at + timedelta(hours=sla_hours(priority))


def is_overdue(created_at, priority, now):
    """工单在 now 时刻是否已经超出 SLA。

    到达截止时间的那一刻就算超时。
    """
    return now > due_at(created_at, priority)
