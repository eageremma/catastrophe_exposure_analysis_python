import numpy as np
import pandas as pd

def add_risk_score(df: pd.DataFrame) -> pd.DataFrame:
    """Add a simple catastrophe exposure risk score and category."""
    df = df.copy()

    hazard_weight = {"Low": 1, "Medium": 2, "High": 3, "Very High": 4}
    occupancy_weight = {
        "Residential": 1.00,
        "Commercial": 1.20,
        "Retail": 1.30,
        "Industrial": 1.50,
        "Public Sector": 1.10
    }

    df["hazard_weight"] = df["hazard_zone"].map(hazard_weight)
    df["occupancy_weight"] = df["occupancy_type"].map(occupancy_weight)

    df["risk_score"] = (
        df["hazard_weight"].fillna(0)
        * df["occupancy_weight"].fillna(0)
        * np.log1p(df["total_insured_value"])
    ).round(3)

    valid_scores = df.loc[df["risk_score"] > 0, "risk_score"]
    q50, q80, q95 = valid_scores.quantile([0.50, 0.80, 0.95])

    def classify_score(x):
        if x <= 0 or pd.isna(x):
            return "Unclassified"
        if x <= q50:
            return "Low Risk"
        elif x <= q80:
            return "Medium Risk"
        elif x <= q95:
            return "High Risk"
        return "Critical Accumulation"

    df["risk_category"] = df["risk_score"].apply(classify_score)
    return df
