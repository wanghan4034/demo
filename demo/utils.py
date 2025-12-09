"""
Utility functions for the demo project.
"""

from pathlib import Path
from typing import Union

import pandas as pd


def load_data(csv_path: Union[str, Path]) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters
    ----------
    csv_path : str or Path
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded data.
    """
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    df = pd.read_csv(csv_path)
    return df


def summarize_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute simple statistics for all numeric columns in the DataFrame.

    For each numeric column, compute:
    - count
    - mean
    - standard deviation
    - min
    - max

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.

    Returns
    -------
    pd.DataFrame
        Summary statistics table.
    """
    # select only numeric columns
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        raise ValueError("No numeric columns found in the input DataFrame.")

    summary = numeric_df.agg(["count", "mean", "std", "min", "max"]).T
    summary = summary.reset_index().rename(columns={"index": "column"})
    return summary