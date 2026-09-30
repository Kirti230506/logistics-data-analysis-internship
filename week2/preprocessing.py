
# WEEK 2: LOGISTICS DATA PREPROCESSING
# YuvaIntern - Logistics Data Analyst
# Dataset: DataCo Smart Supply Chain

import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 1. DATA COLLECTION
file_path = "DataCoSupplyChainDataset.csv"

if not os.path.exists(file_path):
    raise FileNotFoundError(
        "Dataset not found. Place the CSV file "
        "in the same folder as this Python script."
    )

df = pd.read_csv(file_path, encoding="latin1", low_memory=False)

print("\n--- DATA COLLECTION ---")
print("Dataset shape:", df.shape)
print("\nFirst five records:")
print(df.head())

# 2. INITIAL DATA INSPECTION
print("\n--- DATA INSPECTION ---")
print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum().sort_values(ascending=False).head(20))

print("\nDuplicate records:", df.duplicated().sum())

# Save original dimensions for comparison
original_rows = len(df)

# 3. DATA CLEANING
# Replace empty strings and whitespace-only values with NA.
df = df.replace(r"^\s*$", pd.NA, regex=True)

# Remove exact duplicate rows.
df = df.drop_duplicates()

print("\n--- DUPLICATE REMOVAL ---")
print("Rows before:", original_rows)
print("Rows after:", len(df))
print("Duplicates removed:", original_rows - len(df))

# 4. DATA TYPE CONVERSION
# Actual column names used in the DataCo dataset.
date_columns = [
    "order date (DateOrders)",
    "shipping date (DateOrders)"
]

for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(
            df[col], errors="coerce"
        )

# 5. HANDLE MISSING VALUES
print("\n--- MISSING VALUE HANDLING ---")

# Numeric fields suitable for this demonstration.
numeric_columns = [
    "Order Item Quantity",
    "Sales",
    "Order Item Total",
    "Days for shipping (real)",
    "Days for shipment (scheduled)"
]

numeric_columns = [
    c for c in numeric_columns
    if c in df.columns
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    if df[col].notna().any():
        df[col] = df[col].fillna(df[col].median())

# Fill missing values in selected categorical fields.
categorical_columns = [
    "Shipping Mode",
    "Market",
    "Customer Segment"
]

categorical_columns = [
    c for c in categorical_columns
    if c in df.columns
]

for col in categorical_columns:
    df[col] = df[col].astype("string").str.strip()
    df[col] = df[col].replace("", pd.NA)
    if not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

print("Missing values after selected imputations:")
print(df.isnull().sum().sort_values(ascending=False).head(20))

# 6. OUTLIER DETECTION USING IQR
print("\n--- OUTLIER DETECTION ---")

outlier_columns = [
    "Sales",
    "Order Item Total",
    "Order Item Quantity",
    "Days for shipping (real)"
]

outlier_columns = [
    c for c in outlier_columns
    if c in df.columns
]

outlier_summary = []

for col in outlier_columns:
    values = df[col].dropna()
    if values.empty:
        continue

    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    mask = (df[col] < lower) | (df[col] > upper)

    outlier_summary.append({
        "column": col,
        "lower_limit": lower,
        "upper_limit": upper,
        "potential_outliers": int(mask.sum())
    })

    print(f"{col}: {int(mask.sum())} potential outliers")

# Save outlier results for review.
pd.DataFrame(outlier_summary).to_csv(
    "outlier_summary.csv", index=False
)

# Do not automatically delete potential outliers.
# They may represent genuine logistics events.

# 7. NORMALIZATION USING MIN-MAX SCALING
print("\n--- NORMALIZATION ---")

scale_columns = [
    "Order Item Quantity",
    "Sales",
    "Order Item Total",
    "Days for shipping (real)"
]

scale_columns = [
    c for c in scale_columns
    if c in df.columns
    and pd.api.types.is_numeric_dtype(df[c])
    and df[c].notna().any()
]

# Keep original values and create separate scaled columns.
scaler = MinMaxScaler()

for col in scale_columns:
    valid = df[col].notna()
    scaled_col = col + "_scaled"

    df[scaled_col] = pd.NA
    df.loc[valid, scaled_col] = (
        scaler.fit_transform(df.loc[valid, [col]])
        .ravel()
    )

print("Created scaled columns:")
print([c + "_scaled" for c in scale_columns])

# 8. CATEGORICAL DATA PREPARATION
# Encode only selected low-cardinality categories.
encode_columns = [
    c for c in ["Shipping Mode", "Customer Segment"]
    if c in df.columns
]

if encode_columns:
    df = pd.get_dummies(
        df,
        columns=encode_columns,
        drop_first=True,
        dtype=int
    )

# 9. FINAL VALIDATION
print("\n--- FINAL VALIDATION ---")
print("Final dataset shape:", df.shape)
print("\nRemaining missing values:")
print(df.isnull().sum().sort_values(ascending=False).head(20))

print("\nFinal descriptive statistics:")
print(df.describe(include="all"))

# 10. SAVE PREPROCESSED DATA
df.to_csv("logistics_preprocessed.csv", index=False)

print("\nPreprocessing completed.")
print("Output: logistics_preprocessed.csv")
print("Outlier report: outlier_summary.csv")
