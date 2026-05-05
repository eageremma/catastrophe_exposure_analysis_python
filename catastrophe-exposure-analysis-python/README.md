# Catastrophe Exposure Analysis Portfolio Project

## Project overview

This project analyses a simulated property insurance exposure portfolio dataset containing 15,000 property locations.  
It demonstrates a practical catastrophe exposure analytics workflow: data generation, cleaning, validation, risk scoring, exposure aggregation, and portfolio concentration visualisation.

## Business problem

Insurers and reinsurers need to understand where insured values are concentrated, which locations sit in higher hazard zones, and whether the portfolio has dangerous geographic or occupancy-based accumulation.

## What this project does

1. Generates simulated UK-style property exposure data.
2. Adds realistic data-quality issues such as missing postcodes, invalid coordinates, duplicated locations, inconsistent occupancy labels, and negative insured values.
3. Cleans and validates exposure records.
4. Calculates total insured value.
5. Creates a simple catastrophe exposure risk score.
6. Aggregates exposure by region, postcode, occupancy, hazard zone, and risk category.
7. Produces static charts and an interactive portfolio map.
8. Writes portfolio-ready outputs for review.

## Dataset

The core simulated exposure fields include:

- policy_id
- location_id
- postcode
- latitude
- longitude
- region
- country
- occupancy_type
- construction_type
- year_built
- building_value
- contents_value
- business_interruption_value
- total_insured_value
- hazard_zone
- risk_score
- risk_category

## Key results

- Deduplicated records: 15,000
- Total insured value: £35,397,643,701
- Largest region by TIV: Greater London
- Largest postcode by TIV: WS84 7EU
- TIV share in High or Very High hazard zones: 23.6%
- Regional HHI concentration index: 0.1164

## Folder structure

```text
data/
  raw/
  processed/
outputs/
  charts/
  maps/
  tables/
  reports/
src/
notebooks/
```

## Recommended next steps

- Replace simulated exposure data with real policy or address-level exposure data.
- Join property coordinates to official flood, windstorm, wildfire, or earthquake hazard layers.
- Add vulnerability curves and event loss calculations.
- Build a Streamlit dashboard for interactive portfolio review.
- Add reinsurance structures and estimate gross/net exposure.
