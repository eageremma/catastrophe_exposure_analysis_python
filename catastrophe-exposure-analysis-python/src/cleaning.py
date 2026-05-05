import pandas as pd
import numpy as np

def clean_exposure_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardise property exposure data."""
    df = df.copy()

    df["postcode"] = df["postcode"].astype("string").str.upper().str.replace(r"\s+", " ", regex=True).str.strip()
    df.loc[df["postcode"].isin(["<NA>", "NAN", "NONE", ""]), "postcode"] = pd.NA

    occupancy_map = {
        "res": "Residential",
        "residential": "Residential",
        "residential property": "Residential",
        "commercial property": "Commercial",
        "commercial": "Commercial",
        "factory": "Industrial",
        "industrial": "Industrial",
        "shop": "Retail",
        "retail": "Retail",
        "public": "Public Sector",
        "public sector": "Public Sector"
    }

    df["occupancy_type"] = df["occupancy_type"].astype("string").str.lower().str.strip().replace(occupancy_map)

    value_cols = ["building_value", "contents_value", "business_interruption_value"]
    for col in value_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
        df.loc[df[col] < 0, col] = 0

    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

    valid_lat = df["latitude"].between(49.5, 61.0)
    valid_lon = df["longitude"].between(-8.8, 2.1)
    df.loc[~(valid_lat & valid_lon), ["latitude", "longitude"]] = np.nan

    df["total_insured_value"] = df[value_cols].sum(axis=1).round(2)
    df = df.drop_duplicates(subset=["location_id"], keep="first").copy()

    return df
