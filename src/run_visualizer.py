import pandas as pd
import os
from src.visualizer import (
    plot_indicator_over_time,
    plot_multiple_countries,
)

DATA = "data.csv"
INDICATOR_NAME = "Probability (%) of dying between age 30 and exact age 70 from any of cardiovascular disease, cancer, diabetes, or chronic respiratory disease"

csv_path = os.path.join(os.path.dirname(__file__), "..", "data", DATA)
df = pd.read_csv(csv_path)


plot_indicator_over_time(
    df,
    indicator=INDICATOR_NAME,
    country="Mexico",
    save_path="plots/probabilidad_muerte_cronica_mexico.png",
)

plot_indicator_over_time(
    df,
    indicator=INDICATOR_NAME,
    country="United States of America",
    save_path="plots/probabilidad_muerte_cronica_usa.png",
)

plot_indicator_over_time(
    df,
    indicator=INDICATOR_NAME,
    country="Colombia",
    save_path="plots/probabilidad_muerte_cronica_colombia.png",
)

plot_indicator_over_time(
    df,
    indicator=INDICATOR_NAME,
    country="Japan",
    save_path="plots/probabilidad_muerte_japon.png",
)


plot_multiple_countries(
    df,
    indicator="Probability (%) of dying between age 30 and exact age 70 from any of cardiovascular disease, cancer, diabetes, or chronic respiratory disease",
    countries=["Colombia", "Mexico", "United States of America", "Japan"],
)


print("Gráficos generados satisfactoriamente.")
