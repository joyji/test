"""时长格式化。"""


def format_duration(seconds):
    """把秒数格式化成中文时长，例如 3900 -> "1小时5分"。

    >>> format_duration(3900)
    '1小时5分'
    >>> format_duration(90000)
    '1天1小时'
    >>> format_duration(45)
    '45秒'
    """
    seconds = int(seconds)
    days, rest = divmod(seconds, 86400)
    hours, rest = divmod(rest, 3600)
    minutes = rest // 60

    if not (days or hours or minutes):
        return f"{seconds}秒"

    parts = []
    if days:
        parts.append(f"{days}天")
    if hours:
        parts.append(f"{hours}小时")
    if minutes:
        parts.append(f"{minutes}分")
    return "".join(parts)
