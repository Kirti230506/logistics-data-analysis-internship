# Week 2: Logistics Data Preprocessing

## Internship
YuvaIntern - Logistics Data Analyst Intern

## Objective
To demonstrate data collection, cleaning and preprocessing for logistics analysis using Python.

## Dataset
DataCo Smart Supply Chain dataset.
Source: https://www.kaggle.com/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis/kernels

## Technologies
- Python
- Pandas
- Scikit-learn

## Preprocessing steps
1. Load and inspect the CSV dataset.
2. Check data types, missing values and duplicate records.
3. Remove exact duplicate rows.
4. Convert date fields to datetime.
5. Handle selected missing numeric and categorical values.
6. Identify potential outliers using the IQR method.
7. Normalize selected numerical variables using Min-Max scaling.
8. Encode selected categorical variables.
9. Validate and save the processed dataset.

## How to run
Install dependencies:

```bash
pip install pandas scikit-learn
```

Place DataCoSupplyChainDataset.csv in the same folder as preprocessing.py, then run:

```bash
python preprocessing.py
```

## Output
- logistics_preprocessed.csv
- outlier_summary.csv

## Notes
The script is a demonstration of a preprocessing workflow. Review the actual dataset and verify the cleaning results before using the output for further analysis.
