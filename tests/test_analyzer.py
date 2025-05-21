import pandas as pd
import pytest
from src.analyzer import (
    count_by_column,
    mean_by_group,
    top_n_values,
    filter_by_condition,
)


def test_count_by_column_returns_correct_counts():
    data = {"género": ["F", "M", "F", "M", "F"]}
    df = pd.DataFrame(data)

    result = count_by_column(df, "género")
    assert result["F"] == 3
    assert result["M"] == 2
    assert result.index.tolist() == ["F", "M"]


def test_count_by_column_raises_for_missing_column():
    df = pd.DataFrame({"edad": [20, 30]})
    with pytest.raises(ValueError):
        count_by_column(df, "peso")


def test_mean_by_group_returns_correct_means():
    data = {"género": ["F", "M", "F"], "edad": [20, 30, 40]}
    df = pd.DataFrame(data)

    result = mean_by_group(df, "género", "edad")
    assert result["F"] == 30
    assert result["M"] == 30


def test_mean_by_group_raises_for_missing_column():
    df = pd.DataFrame({"género": ["F"], "edad": [25]})
    with pytest.raises(ValueError):
        mean_by_group(df, "género", "peso")


def test_mean_by_group_raises_for_non_numeric_target():
    df = pd.DataFrame({"tipo": ["A", "B"], "nombre": ["Juan", "Ana"]})
    with pytest.raises(TypeError):
        mean_by_group(df, "tipo", "nombre")


def test_top_n_values_returns_limited_results():
    data = {"diagnóstico": ["A", "B", "A", "C", "A", "B"]}
    df = pd.DataFrame(data)

    result = top_n_values(df, "diagnóstico", n=2)
    assert list(result.index) == ["A", "B"]
    assert result["A"] == 3
    assert result["B"] == 2


def test_top_n_values_raises_for_missing_column():
    df = pd.DataFrame({"edad": [20, 30]})
    with pytest.raises(ValueError):
        top_n_values(df, "nombre")


def test_filter_by_condition_returns_filtered_dataframe():
    data = {"edad": [25, 40, 60], "peso": [70, 90, 65], "género": ["F", "M", "F"]}
    df = pd.DataFrame(data)

    result = filter_by_condition(df, "edad > 30 and peso < 80")

    assert result.shape == (1, 3)
    assert result.iloc[0]["edad"] == 60
    assert result.iloc[0]["peso"] == 65


def test_filter_by_condition_raises_on_invalid_syntax():
    data = {"edad": [25, 40]}
    df = pd.DataFrame(data)

    with pytest.raises(ValueError):
        filter_by_condition(df, "edad >>> 30")  # Invalid syntax
