"""Recompute the financial comparison from SEC filing inputs in USD millions.

Run python3 analysis.py to print the report's table as CSV.
"""

import csv
import sys
from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class FiscalYear:
    end: date
    revenue: int | None
    net_income: int | None


# Apple Consolidated Statements of Operations and Microsoft Income Statements.
# FY2023 Forms 10-K supply FY2021–FY2023. FY2026 Forms 10-K supply FY2024–FY2026.
# FY2021 is used only as the revenue baseline for FY2022 growth.
APPLE = (
    FiscalYear(date(2021, 9, 25), 365817, None),
    FiscalYear(date(2022, 9, 24), 394328, 99803),
    FiscalYear(date(2023, 9, 30), 383285, 96995),
    FiscalYear(date(2024, 9, 28), 391035, 93736),
    FiscalYear(date(2025, 9, 27), 416161, 112010),
    FiscalYear(date(2026, 9, 26), 478834, 132175),
)
MICROSOFT = (
    FiscalYear(date(2021, 6, 30), 168088, None),
    FiscalYear(date(2022, 6, 30), 198270, 72738),
    FiscalYear(date(2023, 6, 30), 211915, 72361),
    FiscalYear(date(2024, 6, 30), 245122, 88136),
    FiscalYear(date(2025, 6, 30), 281724, 101832),
    FiscalYear(date(2026, 6, 30), 331839, 133749),
)

METRICS = ("Fiscal year end", "Revenue (USD billions)", "YoY growth", "Net margin")
COLUMNS = ("FY",) + tuple(
    f"{company} {metric}" for company in ("Apple", "Microsoft") for metric in METRICS
)


def percentage(numerator: int | None, denominator: int | None) -> str:
    if numerator is None or denominator is None or denominator == 0:
        return "n/a"
    return f"{Decimal(numerator) * 100 / Decimal(denominator):.1f}%"


def metrics(prior: FiscalYear, current: FiscalYear) -> tuple[str, ...]:
    revenue = current.revenue
    change = None if revenue is None or prior.revenue is None else revenue - prior.revenue
    return (
        f"{current.end:%b} {current.end.day}, {current.end.year}",
        "n/a" if revenue is None else f"{Decimal(revenue) / 1000:.1f}",
        percentage(change, prior.revenue),
        percentage(current.net_income, revenue),
    )


def report_rows() -> list[tuple[str, ...]]:
    apple_years = zip(APPLE, APPLE[1:])
    microsoft_years = zip(MICROSOFT, MICROSOFT[1:])
    return [
        (str(apple.end.year), *metrics(apple_prior, apple), *metrics(microsoft_prior, microsoft))
        for (apple_prior, apple), (microsoft_prior, microsoft)
        in zip(apple_years, microsoft_years, strict=True)
    ]


if __name__ == "__main__":
    writer = csv.writer(sys.stdout)
    writer.writerow(COLUMNS)
    writer.writerows(report_rows())
