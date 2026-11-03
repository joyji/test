import unittest
from datetime import datetime, timedelta

from ticketkit import (
    due_at,
    format_duration,
    is_overdue,
    parse_priority,
    sla_hours,
    summarize,
)


class PriorityTest(unittest.TestCase):
    def test_standard_codes(self):
        self.assertEqual(parse_priority("P1"), "P1")
        self.assertEqual(parse_priority(" P3 "), "P3")

    def test_aliases(self):
        self.assertEqual(parse_priority("紧急"), "P1")
        self.assertEqual(parse_priority("low"), "P4")

    def test_unknown(self):
        with self.assertRaises(ValueError):
            parse_priority("P9")

    def test_sla_hours(self):
        self.assertEqual(sla_hours("P2"), 8)


class SlaTest(unittest.TestCase):
    def setUp(self):
        self.created = datetime(2026, 11, 3, 9, 0)

    def test_due_at(self):
        self.assertEqual(due_at(self.created, "P1"), datetime(2026, 11, 3, 13, 0))

    def test_not_overdue(self):
        now = self.created + timedelta(hours=1)
        self.assertFalse(is_overdue(self.created, "P1", now))

    def test_overdue(self):
        now = self.created + timedelta(hours=5)
        self.assertTrue(is_overdue(self.created, "P1", now))


class FormatTest(unittest.TestCase):
    def test_hours_minutes(self):
        self.assertEqual(format_duration(3900), "1小时5分")

    def test_days_hours(self):
        self.assertEqual(format_duration(90000), "1天1小时")


class ReportTest(unittest.TestCase):
    def test_summarize(self):
        tickets = [
            {"id": 1, "status": "open"},
            {"id": 2, "status": "closed"},
            {"id": 3, "status": "open"},
        ]
        self.assertEqual(
            summarize(tickets),
            {"total": 3, "by_status": {"open": 2, "closed": 1}},
        )


if __name__ == "__main__":
    unittest.main()
