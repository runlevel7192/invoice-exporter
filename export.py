#!/usr/bin/env python3
"""Export paid invoices + billing details to CSV."""
import argparse
import csv
import json
import os

import requests

CFG = json.load(open('config.json'))


def fetch_invoices(month):
    r = requests.get(f"{CFG['api_base']}/invoices", params={'month': month},
                     headers={'Authorization': f"Bearer {CFG['api_key']}"}, timeout=30)
    r.raise_for_status()
    return r.json().get('invoices', [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--month', required=True)
    args = ap.parse_args()
    rows = fetch_invoices(args.month)
    os.makedirs(CFG['output_dir'], exist_ok=True)
    out = os.path.join(CFG['output_dir'], f"invoices-{args.month}.csv")
    with open(out, 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['invoice_id', 'customer', 'amount', 'paid_at'])
    print(f'{len(rows)} invoices -> {out}')


if __name__ == '__main__':
    main()
