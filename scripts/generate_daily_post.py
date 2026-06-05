#!/usr/bin/env python3
"""
Simple local helper for choosing the daily PTAC call training focus.
This does not call an AI model. It selects the correct campaign day and prints the source topic.
Your AI agent should use the printed context to generate the final WhatsApp-ready post.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "data" / "weekly-focus-plan.json"

CAMPAIGN_START_DATE = "2026-06-08"  # Update this to the Monday the campaign starts.
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def business_day_index(start: date, current: date) -> int:
    if current < start:
        return 0
    days = 0
    d = start
    while d <= current:
        if d.weekday() < 5:
            days += 1
        d = date.fromordinal(d.toordinal() + 1)
    return max(days - 1, 0)


def main() -> None:
    plan = json.loads(PLAN_PATH.read_text(encoding="utf-8"))
    start = date.fromisoformat(CAMPAIGN_START_DATE)
    today = date.today()
    idx = business_day_index(start, today)

    if idx >= 15:
        idx = 14

    week_number = idx // 5 + 1
    day_index = idx % 5
    week = plan["weeks"][week_number - 1]
    topic = week["daily_topics"][day_index]

    output = {
        "campaign_title": plan["campaign_title"],
        "week": week_number,
        "week_theme": week["theme"],
        "day": topic["day"],
        "focus_title": topic["title"],
        "behavior": topic["behavior"],
        "required_greeting": "Thank you for choosing Precision Tune Auto Care, my name is [employee’s name], who do I have the pleasure of speaking with?"
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
