import pytest
import pandas as pd
import os
from src.visualizer import (
    plot_indicator_over_time,
    plot_multiple_countries,
)


def test_plot_indicator_over_time_creates_file(tmp_path):
    data = {
        "Indicator": ["Test Indicator"] * 6,
        "Location": ["Testland"] * 6,
        "Period": [2018, 2019, 2020, 2018, 2019, 2020],
        "Dim1": ["Male", "Male", "Male", "Female", "Female", "Female"],
        "FactValueNumeric": [5.1, 5.3, 5.5, 4.8, 4.9, 5.0],
    }
    df = pd.DataFrame(data)

    file_path = "tests/test_plots/test_plot.png"

    plot_indicator_over_time(
        df, indicator="Test Indicator", country="Testland", save_path=str(file_path)
    )

    assert os.path.exists(file_path), "The plot file was not created."
    os.remove(file_path)


def test_plot_indicator_over_time_without_required_columns():
    data = {
        "Indicator": ["Test Indicator"],
        "Location": ["Testland"],
        # 'Period' and 'FactValueNumeric' missing
    }
    df = pd.DataFrame(data)
    file_path = "tests/test_plots/test_indicator_over_time.png"

    with pytest.raises(ValueError):
        plot_indicator_over_time(df, "Test Indicator", "Testland", save_path=file_path)


def test_plot_indicator_over_time_no_matching_data():

    data = {
        "Indicator": ["Another Indicator", "Another Indicator"],
        "Location": ["Otherland", "Otherland"],
        "Period": [2020, 2021],
        "FactValueNumeric": [1.0, 2.0],
    }
    df = pd.DataFrame(data)
    file_path = "tests/test_plots/test_indicator_over_time.png"

    with pytest.raises(ValueError):
        plot_indicator_over_time(df, "Test Indicator", "Testland", save_path=file_path)


def test_plot_multiple_countries_creates_file():
    data = {
        "Indicator": ["Test Indicator"] * 12,
        "Location": ["Aland", "Aland", "Aland", "Borland", "Borland", "Borland"] * 2,
        "Period": [2018, 2019, 2020] * 4,
        "Dim1": ["Male", "Female", "Both sexes"] * 4,
        "FactValueNumeric": [10.0, 9.0, 9.5, 12.0, 11.0, 11.5] * 2,
    }
    df = pd.DataFrame(data)
    file_path = "tests/test_plots/test_comparacion_paises.png"

    plot_multiple_countries(
        df,
        indicator="Test Indicator",
        countries=["Aland", "Borland"],
        save_path=file_path
    )

    assert os.path.exists(file_path)
    os.remove(file_path)
