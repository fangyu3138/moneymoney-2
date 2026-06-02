---
name: micro-finance-expense-optimizer
description: Standard workflow for turning daily hidden expenses into monthly/yearly cost, opportunity cost, compound future value, salary allocation, CSV expense classification, and dream BOM purchasing-power breakdown. Use when building or explaining a personal micro-finance dashboard, latte-factor calculator, expense optimizer, or long-term habit cost projection.
---

# Micro-Finance Expense Optimizer

## Goal

Convert small habitual expenses into visible financial tradeoffs. Use this workflow to clean daily expense data, classify necessary spending and hidden expenses, standardize costs by month/year, model partial consumption downgrade scenarios, and translate future value into concrete purchasing power.

## Inputs

- Monthly salary in TWD.
- Necessary monthly expenses or necessary-expense percentage.
- Daily, weekly, and fixed monthly hidden expense items.
- Optional raw bookkeeping CSV with `date`, `description`, and `amount` columns.
- Downgrade ratio from 0% to 100%.
- Annual investment return from 1% to 10%.
- Observation period from 1 to 10 years.

## Workflow

1. Parse expense records from direct inputs or CSV.
2. Classify each CSV row by keyword:
   - Necessary expenses: rent, utilities, insurance, loans, transit, groceries, and equivalent Chinese terms.
   - Hidden expenses: coffee, drinks, subscriptions, delivery, snacks, late-night food, and equivalent Chinese terms.
   - Other rows stay unclassified and do not automatically enter the hidden-expense model.
3. Convert mixed-frequency spending into monthly values.
4. Apply the downgrade ratio to estimate newly available monthly savings.
5. Project future value using monthly contribution compounding.
6. Build a salary allocation view with necessary expenses, remaining hidden expenses, and free cash/savings.
7. Convert the ending future value into dream BOM purchasing power.
8. Show a selected-goal timeline based on current monthly savings.
9. Show a pain-level hint based on the downgrade ratio.
10. Summarize CSV classification counts and the largest hidden-expense row after import.

## Formulas

```text
E_month = (E_day * 30.4) + (E_week * 4.33) + E_fixed_monthly
```

```text
E_year = E_month * 12
```

```text
E_month_saved = E_hidden_month * downgrade_ratio
```

```text
FV = E_month_saved * (((1 + r / 12)^(12n) - 1) / (r / 12))
```

When `r = 0`:

```text
FV = E_month_saved * 12 * n
```

## Dream BOM Rules

Use local, editable assumptions rather than pretending prices are universal.

- Bangkok travel set: one round-trip ticket, five days of BTS transit, and lodging.
- Taitung two-day one-night trip: round-trip transport, one-night lodging, food, and local transport.
- Europe travel set: long-haul round-trip ticket, lodging, city/intercity transit, and attraction/food buffer.
- Badminton equipment: high-end racket, string/grip, and cover.
- Concert visit: one ticket plus transport and small on-site spending, with editable seat-price assumptions.
- Island buffet visit: estimate one meal at Shin Yeh Island Buffet as an editable short-term goal.

## Output Requirements

- Show monthly hidden expense before optimization.
- Show newly available monthly savings after downgrade.
- Show ending future value for the selected period and return.
- Show salary allocation as necessary expenses, remaining hidden expenses, and surplus.
- Show comparison between current behavior and optimized compounding path.
- Show dream BOM quantities and remaining purchasing power.
- Show how many months are needed to reach a selected dream BOM target.
- Show pain level for the selected downgrade ratio.
- Show CSV classification summary when imported data exists.

## Implementation Notes

- Keep calculations client-side for privacy when building a static web dashboard.
- Prefer native CSS/SVG charts for static GitHub Pages delivery; use Chart.js or Plotly only when external dependencies are acceptable.
- Format all money values as TWD.
- Treat the workflow as educational and decision-support only, not financial advice.
