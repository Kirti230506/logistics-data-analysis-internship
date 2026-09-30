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
## Actual Program Output

Original dataset: 180519 rows × 53 columns

Final dataset: 180519 rows × 60 columns

The program completed successfully and generated
`logistics_preprocessed.csv`.

### Screenshot

![Successful program output]
<img width="907" height="537" alt="Screenshot 2026-09-30 211324" src="https://github.com/user-attachments/assets/d6c3c998-28e4-4f3f-99f1-792f99ad3fe9" />
