# invoice-exporter

Exports the month's paid invoices, with customer billing details, to CSV
for the accounting team.

## Usage

```
pip install -r requirements.txt
python export.py --month 2026-09
```

Reads API access from `config.json`.
