import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def plot_indicator_over_time(
    df: pd.DataFrame,
    indicator: str,
    country: str,
    save_path: str = "plots/indicator_over_time.png",
) -> None:
    """
    Plot time series of an indicator in a country, grouped by Dim1.
    """
    if not all(
        col in df.columns
        for col in ["Indicator", "Location", "Period", "FactValueNumeric"]
    ):
        raise ValueError(
            "Required columns ('Indicator', 'Location', 'Period', 'FactValueNumeric') are missing from the DataFrame."
        )

    filtered = df[
        (df["Indicator"] == indicator)
        & (df["Location"] == country)
        & (~df["FactValueNumeric"].isna())
    ].copy()

    if filtered.empty:
        raise ValueError(
            "No matching data found for the specified indicator and country."
        )

    filtered["Period"] = pd.to_numeric(filtered["Period"], errors="coerce")
    filtered = filtered.dropna(subset=["Period"])
    filtered["Period"] = filtered["Period"].astype(int)

    plt.figure(figsize=(10, 6))

    palette = {"Female": "#1f77b4", "Male": "#ff7f0e", "Both sexes": "#2ca02c"}
    hue_order = ["Female", "Male", "Both sexes"]

    sns.lineplot(
        data=filtered,
        x="Period",
        y="FactValueNumeric",
        hue="Dim1",
        hue_order=hue_order,
        palette=palette,
        marker="o",
    )

    plt.title(f"{indicator}\n{country} over time")
    plt.xlabel("Year")
    plt.ylabel("FactValueNumeric")
    plt.legend(title="Dim1")
    plt.tight_layout()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()


def plot_multiple_countries(df, indicator, countries, save_path="plots/comparacion_paises.png"):
    palette = {
        "Female": "#1f77b4",
        "Male": "#ff7f0e",
        "Both sexes": "#2ca02c"
    }
    hue_order = ["Female", "Male", "Both sexes"]

    fig, axes = plt.subplots(1, len(countries), figsize=(6 * len(countries), 6), sharey=True)

    for ax, country in zip(axes, countries):
        filtered = df[
            (df["Indicator"] == indicator) &
            (df["Location"] == country) &
            (~df["FactValueNumeric"].isna())
        ].copy()

        filtered["Period"] = pd.to_numeric(filtered["Period"], errors="coerce")
        filtered = filtered.dropna(subset=["Period"])
        filtered["Period"] = filtered["Period"].astype(int)

        sns.lineplot(
            data=filtered,
            x="Period",
            y="FactValueNumeric",
            hue="Dim1",
            hue_order=hue_order,
            palette=palette,
            marker="o",
            ax=ax
        )
        ax.set_title(country)
        ax.set_xlabel("Year")
        if ax == axes[0]:
            ax.set_ylabel("Probability of premature death (%)")
        else:
            ax.set_ylabel("")

    plt.suptitle(indicator, fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(save_path)
    plt.close()
