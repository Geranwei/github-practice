# Apple vs. Microsoft five-year comparison

## Approval and handoff

Pause after saving this approved plan. Wait for separate authorization before retrieving financial data, writing analysis code, or creating either report.

## Data and calculations

- Cover FY2022–FY2026 for each company. Show each company’s actual fiscal year-end date for every row and compare by fiscal-year label. Note the different fiscal calendars and Apple’s 53-week FY2023.
- Use Apple’s consolidated **Total net sales**, Microsoft’s consolidated **Total revenue**, and each company’s consolidated **Net income**. Use FY2026 Forms 10-K for FY2024–FY2026 and FY2023 Forms 10-K for FY2022–FY2023 and the FY2021 revenue baseline. Check intervening filings and amendments for revisions to consolidated figures. Link each reported figure to its applicable SEC filing and identify the statement used. [Apple FY2026](https://www.sec.gov/Archives/edgar/data/320193/000032019326000026/aapl-20260926.htm) · [Apple FY2023](https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm) · [Microsoft FY2026](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm) · [Microsoft FY2023](https://www.sec.gov/Archives/edgar/data/789019/000095017023035122/msft-20230630.htm)
- Calculate annual revenue growth as `(current revenue ÷ prior-year revenue − 1) × 100` and net margin as `net income ÷ revenue × 100`. Use FY2021 revenue only for FY2022 growth. Calculate at filing precision and display revenue in USD billions and rates as percentages, each to one decimal place.
- Display `n/a` for unavailable inputs and ratios with missing inputs or a zero denominator. Explain each `n/a` in a table note and leave a gap for it in charts.

## Reports and checks

- Keep `task.md`, `report.html`, and `report.pdf` together in `apple-microsoft-comparison/`. Build a self-contained HTML report with a side-by-side table, one chart per metric, a brief comparison, and SEC source links. Generate the PDF from that HTML using print styles.
- Reconcile inputs and fiscal year-end dates to the cited filings. Independently recompute available ratios, including FY2022 growth, and check units, signs, rounding, and `n/a` handling.
- Open the HTML offline at desktop and narrow widths. Render every PDF page and inspect page breaks, clipping, and chart legibility. Confirm that table values, fiscal year-end dates, `n/a` entries, and clickable SEC links agree across both formats.
