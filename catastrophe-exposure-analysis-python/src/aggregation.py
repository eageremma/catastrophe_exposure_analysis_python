import pandas as pd

def aggregate_by_region(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("region")
        .agg(
            location_count=("location_id", "count"),
            total_tiv=("total_insured_value", "sum"),
            avg_tiv=("total_insured_value", "mean"),
            max_tiv=("total_insured_value", "max"),
            avg_risk_score=("risk_score", "mean")
        )
        .sort_values("total_tiv", ascending=False)
        .reset_index()
    )

def aggregate_by_hazard(df: pd.DataFrame) -> pd.DataFrame:
    out = (
        df.groupby("hazard_zone")
        .agg(
            location_count=("location_id", "count"),
            total_tiv=("total_insured_value", "sum"),
            avg_tiv=("total_insured_value", "mean"),
            avg_risk_score=("risk_score", "mean")
        )
        .reset_index()
    )
    out["tiv_share"] = out["total_tiv"] / out["total_tiv"].sum()
    return out
