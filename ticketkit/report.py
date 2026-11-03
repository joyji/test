"""工单统计。"""


def summarize(tickets):
    """按状态统计工单数量。

    tickets 是字典列表，每个字典至少包含 "status" 字段。
    返回 {"total": 总数, "by_status": {状态: 数量}}。
    """
    by_status = {}
    for ticket in tickets:
        status = ticket["status"]
        by_status[status] = by_status.get(status, 0) + 1
    return {"total": len(tickets), "by_status": by_status}
