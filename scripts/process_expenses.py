#!/usr/bin/env python3
"""Classify bookkeeping CSV rows into necessary and hidden expenses."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


ESSENTIAL_KEYWORDS = {
    "房租",
    "租金",
    "水電",
    "瓦斯",
    "電費",
    "健保",
    "保險",
    "學貸",
    "交通",
    "捷運",
    "公車",
    "雜貨",
    "rent",
    "utility",
    "insurance",
    "loan",
    "grocery",
    "groceries",
}

HIDDEN_KEYWORDS = {
    "咖啡",
    "拿鐵",
    "手搖",
    "飲料",
    "珍奶",
    "訂閱",
    "外送",
    "點心",
    "宵夜",
    "netflix",
    "spotify",
    "disney",
    "youtube",
    "uber eats",
}


def parse_amount(value: str) -> float:
    cleaned = re.sub(r"[^\d.\-]", "", value or "0")
    try:
        return abs(float(cleaned))
    except ValueError:
        return 0.0


def classify(description: str) -> str:
    text = description.lower()
    if any(keyword.lower() in text for keyword in HIDDEN_KEYWORDS):
        return "hidden"
    if any(keyword.lower() in text for keyword in ESSENTIAL_KEYWORDS):
        return "essential"
    return "other"


def process_csv(path: Path) -> dict[str, object]:
    totals = {"essential": 0.0, "hidden": 0.0, "other": 0.0}
    counts = {"essential": 0, "hidden": 0, "other": 0}
    months: set[str] = set()
    rows: list[dict[str, object]] = []

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
      reader = csv.DictReader(handle)
      if not reader.fieldnames:
          raise ValueError("CSV must include headers.")

      field_map = {name.lower(): name for name in reader.fieldnames}
      date_field = next(
          (field_map[name] for name in ("date", "日期") if name in field_map),
          None,
      )
      description_field = next(
          (field_map[name] for name in ("description", "item", "memo", "備註", "項目") if name in field_map),
          None,
      )
      amount_field = next(
          (field_map[name] for name in ("amount", "cost", "金額") if name in field_map),
          None,
      )

      if not description_field or not amount_field:
          raise ValueError("CSV must include description and amount columns.")

      for row in reader:
          date_value = row.get(date_field, "") if date_field else ""
          month_match = re.match(r"^(\d{4})[-/](\d{1,2})", date_value)
          if month_match:
              months.add(f"{month_match.group(1)}-{int(month_match.group(2)):02d}")

          description = row.get(description_field, "")
          amount = parse_amount(row.get(amount_field, "0"))
          category = classify(description)
          totals[category] += amount
          counts[category] += 1
          rows.append({"description": description, "amount": amount, "category": category})

    month_count = max(1, len(months))

    return {
        "monthly_average": {key: round(value / month_count, 2) for key, value in totals.items()},
        "totals": {key: round(value, 2) for key, value in totals.items()},
        "counts": counts,
        "month_count": month_count,
        "rows": rows,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: process_expenses.py <expenses.csv>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 1

    result = process_csv(path)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
