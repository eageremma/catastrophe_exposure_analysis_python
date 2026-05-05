# Executive Report: Catastrophe Exposure Analysis
## 1. Objective

The objective of this project is to build an end-to-end catastrophe exposure analysis workflow using simulated property exposure data. The analysis identifies portfolio concentration by geography, occupancy type, hazard zone, and risk category.

## 2. Data generation

The project generated 15,000 UK-style property exposure records. Each record represents an insured property location with postcode, latitude, longitude, region, occupancy type, construction type, insured values, and hazard zone.

To make the project realistic, controlled data-quality issues were added before cleaning:

- Missing postcodes
- Missing and invalid coordinates
- Inconsistent occupancy labels
- Negative insured values
- Duplicate location records

## 3. Cleaning and validation

The data cleaning process standardised postcodes, normalised occupancy labels, corrected negative financial values, recalculated total insured value, removed duplicate location IDs, and flagged records needing review.

## 4. Portfolio summary

| metric                                        | value           |
|:----------------------------------------------|:----------------|
| Number of records                             | 15,000          |
| Number of valid records                       | 14,761          |
| Number of unique regions                      | 12              |
| Number of unique postcodes                    | 14,876          |
| Total insured value                           | £35,397,643,701 |
| Average TIV                                   | £2,359,843      |
| Median TIV                                    | £594,561        |
| Maximum TIV                                   | £158,570,266    |
| Share of TIV in High + Very High hazard zones | 23.6%           |
| Share of TIV in top 5 regions                 | 63.6%           |

## 5. Key findings

1. The simulated portfolio contains 15,000 deduplicated property locations with total insured value of £35,397,643,701.
2. The largest regional accumulation is Greater London, with £8,060,654,190 of TIV across 3,362 locations.
3. The largest postcode-level accumulation is WS84 7EU in West Midlands, with £158,570,266 of TIV.
4. 23.6% of portfolio TIV sits in High or Very High hazard zones.
5. The highest TIV occupancy segment is Industrial, contributing £18,642,661,709.
6. The regional HHI concentration index is 0.1164; this gives a simple quantitative read on geographic concentration.
7. Critical Accumulation locations account for 17.4% of portfolio TIV.

## 6. Interpretation

The portfolio is materially concentrated in a small number of high-value regions and postcode areas. This matters because catastrophe events are spatially correlated: one flood, windstorm, or earthquake can affect many nearby locations at the same time.

The High and Very High hazard zones deserve special underwriting attention because they combine elevated hazard severity with insured values that could produce large losses.

## 7. Recommended underwriting actions

- Review top postcode accumulations by total insured value.
- Apply tighter underwriting rules for High and Very High hazard zones.
- Investigate the largest individual industrial and commercial risks.
- Monitor regional HHI over time as the book grows.
- Consider accumulation limits by postcode, region, and hazard zone.
- Improve geocoding quality for records missing valid coordinates.

## 8. Limitations

This project uses simulated exposure and hazard data. It is suitable for demonstrating analytical workflow, but not for real underwriting decisions. In production, the model should use verified property exposure data and official hazard layers.
