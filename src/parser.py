import pandas as pd
import re


def normalize_column_name(col):
    """
    Normalize Spanish column names to standardized Spanish identifiers,
    removing units, special characters, and using lowercase with underscores.
    """
    col = col.lower().strip()
    col = re.sub(r"\s+", "_", col)
    col = re.sub(r"\(.*?\)", "", col)  # Remove units like (kg), (cm)
    col = re.sub(r"[^a-z0-9_áéíóúñ]", "", col)  # Keep accents

    keyword_map = {
        "id": "id",
        "nombre": "nombre",
        "sexo": "género",
        "genero": "género",
        "edad": "edad",
        "años": "edad",
        "peso": "peso",
        "altura": "altura",
        "estatura": "altura",
        "bmi": "imc",
        "diagnostico": "diagnóstico",
        "cie10": "diagnóstico",
        "nivel_socioeconomico": "nivel_socioeconómico",
    }

    for keyword, standard in keyword_map.items():
        if col == keyword or col.startswith(keyword + "_"):
            return standard
    return col


def parse_csv(filepath):
    """
    Reads and parses a CSV file, normalizing column names and converting numeric fields.
    """
    try:
        df = pd.read_csv(filepath, encoding="utf-8", on_bad_lines="skip")
    except pd.errors.EmptyDataError:
        return pd.DataFrame()

    # Normalize column names
    df.columns = [normalize_column_name(col) for col in df.columns]

    # Attempt conversion of known numeric fields
    numeric_columns = ["edad", "peso", "altura", "imc"]
    for col in numeric_columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
            df[col] = pd.to_numeric(df[col], errors="coerce", downcast="float")

    return df
