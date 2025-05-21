import pandas as pd


def count_by_column(df: pd.DataFrame, column: str) -> pd.Series:
    """
    Count frequency of each unique value in a column.
    Returns a Series sorted in descending order.
    """
    if column not in df.columns:
        raise ValueError(f"La columna '{column}' no existe en el DataFrame.")
    return df[column].value_counts().sort_values(ascending=False)


def mean_by_group(df: pd.DataFrame, group_col: str, target_col: str) -> pd.Series:
    """
    Calculate the mean of a numeric column grouped by another column.
    Returns a Series sorted in descending order.
    """
    if group_col not in df.columns or target_col not in df.columns:
        raise ValueError(f"Columnas '{group_col}' o '{target_col}' no encontradas.")
    if not pd.api.types.is_numeric_dtype(df[target_col]):
        raise TypeError(f"La columna '{target_col}' no es numérica.")
    return df.groupby(group_col)[target_col].mean().sort_values(ascending=False)


def top_n_values(df: pd.DataFrame, column: str, n: int = 5) -> pd.Series:
    """
    Return the top N most frequent values in a column.
    """
    if column not in df.columns:
        raise ValueError(f"La columna '{column}' no existe en el DataFrame.")
    return df[column].value_counts().head(n)


def filter_by_condition(df: pd.DataFrame, condition: str) -> pd.DataFrame:
    """
    Filter DataFrame based on a condition string.
    Example condition: "edad > 30 and peso < 80"
    """
    try:
        filtered_df = df.query(condition)
    except Exception as e:
        raise ValueError(f"Error al aplicar la condición: {e}")
    return filtered_df
