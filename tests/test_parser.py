import os
import numbers
from src.parser import parse_csv


def test_parse_csv_with_standard_and_variant_columns():
    # Arrange
    sample_data = (
        "ID,Nombre completo,Sexo,Años,Peso (kg),Estatura,BMI,Nivel Socioeconómico\n"
        "1,Juan Medina,M,40,80,180,24.7,3\n"
        "2,Laura Rodriguez Gómez,F,30,65,160,25.4,2\n"
    )
    file_path = "tests/temp_sample.csv"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(sample_data)

    # Act
    df = parse_csv(file_path)

    # Assert - Column name normalization
    expected_columns = [
        "id",
        "nombre",
        "género",
        "edad",
        "peso",
        "altura",
        "imc",
        "nivel_socioeconómico",
    ]
    assert list(df.columns) == expected_columns

    # Assert - Data content and types
    assert df.shape == (2, 8)
    assert df["nombre"].iloc[0] == "Juan Medina"
    assert df["nombre"].iloc[1] == "Laura Rodriguez Gómez"
    assert df["género"].iloc[1] == "F"
    assert df["edad"].iloc[0] == 40.0
    assert isinstance(df["peso"].iloc[1], numbers.Real)
    assert isinstance(df["altura"].iloc[1], numbers.Real)
    assert df["imc"].iloc[1] == 25.4

    # Cleanup
    os.remove(file_path)


def test_parse_csv_with_unknown_columns():
    sample_data = (
        "Código,Fecha de ingreso,Temperatura corporal\n"
        "001,2024-05-10,36.5\n"
        "002,2024-05-11,38.0\n"
    )
    file_path = "tests/temp_unknown.csv"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(sample_data)

    df = parse_csv(file_path)

    # Column names retain accents
    assert "código" in df.columns
    assert "fecha_de_ingreso" in df.columns
    assert "temperatura_corporal" in df.columns
    assert df.shape == (2, 3)

    os.remove(file_path)


def test_parse_csv_with_empty_file():
    empty_file_path = "tests/temp_empty.csv"
    with open(empty_file_path, "w", encoding="utf-8"):
        pass

    df = parse_csv(empty_file_path)

    # Expect an empty DataFrame with no columns
    assert df.empty
    assert df.shape == (0, 0)

    os.remove(empty_file_path)
