from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "seattle_rent.csv"
FIGURES = ROOT / "figures"


def load_data() -> pd.DataFrame:
    """Load and validate the supplied Seattle apartment-rent CSV."""
    df = pd.read_csv(DATA_PATH).rename(
        columns={
            "Community Reporting Area Name": "community",
            "Tract Median Apartment Contract Rent per Unit": "rent_per_unit",
            "Tract Median Apartment Contract Rent per Square Foot": "rent_per_sqft",
            "Year over Year Change in Rent per Unit": "yoy_change_unit",
            "Mixed-Rate or Mixed-Income Apartment in Tract": "mixed_income_count",
            "PROPERTIES": "property_count",
        }
    )
    required = [
        "GEOID", "Year", "community", "rent_per_unit", "rent_per_sqft",
        "yoy_change_unit", "mixed_income_count", "property_count",
    ]
    missing = sorted(set(required) - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    df = df[required].copy()
    numeric = [c for c in required if c not in {"GEOID", "community"}]
    for column in numeric:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    df = df.dropna(subset=numeric + ["community"])
    df = df[df["rent_per_unit"] > 0].copy()
    # The source stores annual rent changes as proportions (for example, 0.05 = 5%).
    df["yoy_change_unit"] = df["yoy_change_unit"] * 100
    return df


def save_figures(df: pd.DataFrame) -> None:
    FIGURES.mkdir(exist_ok=True)
    sns.set_theme(style="whitegrid")

    yearly = df.groupby("Year", as_index=False)["rent_per_unit"].mean()
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=180)
    sns.lineplot(data=yearly, x="Year", y="rent_per_unit", marker="o", ax=ax)
    ax.set(title="Average Seattle apartment rent over time", xlabel="Year", ylabel="Mean rent per unit ($)")
    fig.tight_layout(); fig.savefig(FIGURES / "rent-trend.png", bbox_inches="tight"); plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=180)
    sns.regplot(data=df, x="mixed_income_count", y="rent_per_unit", scatter_kws={"alpha": 0.18}, ax=ax)
    ax.set(title="Mixed-income apartments and median rent", xlabel="Mixed-income apartment count", ylabel="Median rent per unit ($)")
    fig.tight_layout(); fig.savefig(FIGURES / "mixed-income-rent.png", bbox_inches="tight"); plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=180)
    sns.regplot(data=df, x="mixed_income_count", y="yoy_change_unit", scatter_kws={"alpha": 0.18}, ax=ax)
    ax.set(title="Mixed-income apartments and year-over-year rent growth", xlabel="Mixed-income apartment count", ylabel="Year-over-year rent change (%)")
    fig.tight_layout(); fig.savefig(FIGURES / "mixed-income-rent-growth.png", bbox_inches="tight"); plt.close(fig)

    top = df.groupby("community")["rent_per_unit"].mean().nlargest(10).sort_values()
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=180)
    top.plot.barh(ax=ax, color="#4472c4")
    ax.set(title="Ten communities with the highest mean rent", xlabel="Mean rent per unit ($)", ylabel="Community")
    fig.tight_layout(); fig.savefig(FIGURES / "community-rent.png", bbox_inches="tight"); plt.close(fig)

    corr = df[["rent_per_unit", "rent_per_sqft", "yoy_change_unit", "mixed_income_count", "property_count", "Year"]].corr()
    fig, ax = plt.subplots(figsize=(7, 6), dpi=180)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, ax=ax)
    ax.set_title("Correlation matrix of analysis variables")
    fig.tight_layout(); fig.savefig(FIGURES / "correlation-heatmap.png", bbox_inches="tight"); plt.close(fig)


def main() -> None:
    df = load_data()
    save_figures(df)
    features = ["Year", "mixed_income_count", "property_count"]
    X_train, X_test, y_train, y_test = train_test_split(df[features], df["rent_per_unit"], test_size=0.2, random_state=1)
    model = LinearRegression().fit(X_train, y_train)
    print(f"Rows analysed: {len(df)}")
    print(f"Years: {int(df.Year.min())}-{int(df.Year.max())}")
    print(f"Mixed-income/rent correlation: {df['mixed_income_count'].corr(df['rent_per_unit']):.3f}")
    print(f"Mixed-income/rent-growth correlation: {df['mixed_income_count'].corr(df['yoy_change_unit']):.3f}")
    print(f"Random 80/20 test R2: {r2_score(y_test, model.predict(X_test)):.3f}")
    print(f"Random 80/20 test RMSE: {mean_squared_error(y_test, model.predict(X_test)) ** 0.5:.2f}")
    print(f"Saved figures to {FIGURES}")


if __name__ == "__main__":
    main()
