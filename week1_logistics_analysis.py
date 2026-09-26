import pandas as pd

# Load logistics dataset
df = pd.read_csv("logistics_data.csv")

# Basic inspection
print(df.head())
print(df.info())
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Convert dates
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["delivery_date"] = pd.to_datetime(df["delivery_date"], errors="coerce")

# Calculate delivery time
df["delivery_days"] = (
    df["delivery_date"] - df["order_date"]
).dt.days

# Basic KPI
average_delivery_time = df["delivery_days"].mean()

print("Average Delivery Time:",
      round(average_delivery_time, 2), "days")
