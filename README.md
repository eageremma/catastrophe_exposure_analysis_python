# Catastrophe Exposure Analysis in Python

## Project Overview
This project builds an end-to-end catastrophe exposure analytics workflow using 15,000 simulated property insurance records.

## Business Problem
Insurance portfolios can become dangerously concentrated in specific regions, postcodes, occupancy types, or hazard zones. This project identifies those accumulations using Python.

## Tools Used
- Python
- pandas
- numpy
- matplotlib
- folium
- Jupyter Notebook

## Dataset
The dataset contains simulated property exposure records with:
- postcode
- latitude and longitude
- region
- occupancy type
- construction type
- building value
- contents value
- business interruption value
- total insured value
- hazard zone
- risk score
- risk category

## Workflow
1. Generate simulated property exposure data
2. Add realistic data quality issues
3. Clean and validate records
4. Calculate total insured value
5. Score catastrophe risk
6. Aggregate exposure by region, postcode, hazard zone, and occupancy
7. Visualise concentration using charts and maps

## Key Findings
- Total insured value: £35.4bn
- Largest regional accumulation: Greater London
- Share of TIV in High and Very High hazard zones: 23.6%
- Highest TIV occupancy segment: Industrial
- Critical Accumulation share of TIV: 17.4%

## Outputs
The project includes:
- cleaned exposure dataset
- validation summary
- exposure aggregation tables
- static charts
- interactive portfolio map
- executive report
