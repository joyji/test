# ticketkit

IT 服务台工单的小工具集，用于试用 dsh-superagent。

只依赖 Python 3.8+ 标准库。

## 功能

- `parse_priority` / `sla_hours`：解析工单优先级（P1~P4 及别名），返回 SLA 小时数
- `due_at` / `is_overdue`：计算 SLA 截止时间，判断是否超时
- `format_duration`：把秒数格式化成中文时长
- `summarize`：按状态统计工单

## 运行测试

```bash
python3 -m unittest discover -s tests -v
```

## 贡献约定

- 修改行为时同时补充或更新 `tests/` 里的测试
- 提交前确保全部测试通过
