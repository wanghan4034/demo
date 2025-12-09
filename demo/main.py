"""
Entry point for the demo project.

Usage (from project root):

    python -m my_project.main
    python -m my_project.main --csv-path data/example.csv
"""

import argparse
from pathlib import Path

from .utils import load_data, summarize_numeric_columns


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Demo project: load a CSV file and show basic statistics."
    )
    parser.add_argument(
        "--csv-path",
        type=str,
        default="data/example.csv",
        help="Path to the input CSV file (default: data/example.csv).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    csv_path = Path(args.csv_path)

    print(f"[INFO] Loading data from: {csv_path}")
    df = load_data(csv_path)

    print(f"[INFO] Data shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print("[INFO] First few rows:")
    print(df.head())

    print("\n[INFO] Summary of numeric columns:")
    summary = summarize_numeric_columns(df)
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()