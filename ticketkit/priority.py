"""工单优先级解析与对应的 SLA 时长。"""

# 每个优先级要求在多少小时内解决
SLA_HOURS = {
    "P1": 4,
    "P2": 8,
    "P3": 24,
    "P4": 72,
}

# 允许的别名
ALIASES = {
    "紧急": "P1",
    "高": "P2",
    "中": "P3",
    "低": "P4",
    "urgent": "P1",
    "high": "P2",
    "medium": "P3",
    "low": "P4",
}


def parse_priority(text):
    """把用户输入的优先级文本解析成 P1~P4。

    >>> parse_priority("P2")
    'P2'
    >>> parse_priority("紧急")
    'P1'
    """
    value = text.strip()
    if value in SLA_HOURS:
        return value
    if value in ALIASES:
        return ALIASES[value]
    raise ValueError(f"无法识别的优先级：{text!r}")


def sla_hours(priority):
    """返回某个优先级的 SLA 小时数。"""
    return SLA_HOURS[parse_priority(priority)]
