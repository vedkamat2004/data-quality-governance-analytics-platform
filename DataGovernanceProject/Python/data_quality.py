import pandas as pd
from datetime import datetime

# Step 3: Load the dataset
df = pd.read_csv("transactions.csv")

# Display the first 5 rows
print("Preview of the data:")
print(df.head())

# Display dataset information
print("\nDataset Info:")
print(df.info())




# Step 1: Load the dataset
df = pd.read_csv("transactions.csv")

print("=== STEP 4: DATA QUALITY CHECKS ===")

# --------------------------
# 1️⃣ Missing Value Checks
# --------------------------
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values)

# --------------------------
# 2️⃣ Negative Amount Check
# --------------------------
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
negative_amounts = df[df["amount"] < 0]
print("\nNegative Amounts:")
print(negative_amounts)

# --------------------------
# 3️⃣ Duplicate Transaction ID Check
# --------------------------
duplicate_txn = df[df.duplicated("txn_id", keep=False)]
print("\nDuplicate Transaction IDs:")
print(duplicate_txn)

# --------------------------
# 4️⃣ Invalid Date Format Check
# --------------------------
# Convert date column to datetime (errors='coerce' marks bad dates as NaT)
df["parsed_date"] = pd.to_datetime(df["date"], errors="coerce")

invalid_dates = df[df["parsed_date"].isna()]
print("\nInvalid Dates:")
print(invalid_dates)

# --------------------------
# 5️⃣ Future Date Check
# --------------------------
today = datetime.today()

future_dates = df[df["parsed_date"] > today]
print("\nFuture Dates:")
print(future_dates)


# --------------------------
# STEP 5: Export Summary File
# --------------------------

summary = {
    "missing_values": int(missing_values.sum()),
    "negative_amounts": negative_amounts.shape[0],
    "duplicate_txn_id": duplicate_txn.shape[0],
    "invalid_dates": invalid_dates.shape[0],
    "future_dates": future_dates.shape[0]
}

summary_df = pd.DataFrame([
    {"check_name": key, 
     "count": value,
     "status": "fail" if value > 0 else "pass"}
    for key, value in summary.items()
])

summary_df.to_csv("control_results.csv", index=False)

print("\nControl summary saved to control_results.csv")
print(summary_df)


# --------------------------
# STEP 6: Audit Log (Run-Level Status)
# --------------------------

total_errors = sum(summary.values())
run_status = "PASS" if total_errors == 0 else "FAIL"

audit_entry = pd.DataFrame([{
    "run_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "missing_values": summary["missing_values"],
    "negative_amounts": summary["negative_amounts"],
    "duplicate_txn_id": summary["duplicate_txn_id"],
    "invalid_dates": summary["invalid_dates"],
    "future_dates": summary["future_dates"],
    "total_errors": total_errors,
    "run_status": run_status
}])

# Append to log file (create if doesn't exist)
import os
if not os.path.exists("audit_log.csv"):
    audit_entry.to_csv("audit_log.csv", index=False)
else:
    audit_entry.to_csv("audit_log.csv", mode='a', index=False, header=False)

print("\nAudit log updated:")
print(audit_entry)


# --------------------------
# STEP 7: Row-Level PASS/FAIL
# --------------------------

# Row-level missing value check
df["missing_value_fail"] = df.isnull().any(axis=1)

# Row-level negative amount
df["negative_amount_fail"] = df["amount"] < 0

# Row-level duplicate txn_id
df["duplicate_txn_fail"] = df.duplicated("txn_id", keep=False)

# Row-level invalid date
df["invalid_date_fail"] = df["parsed_date"].isna()

# Row-level future date
df["future_date_fail"] = df["parsed_date"] > datetime.today()

# Final row status: PASS only if all checks are false
df["row_status"] = df[[
    "missing_value_fail",
    "negative_amount_fail",
    "duplicate_txn_fail",
    "invalid_date_fail",
    "future_date_fail"
]].any(axis=1).apply(lambda x: "FAIL" if x else "PASS")

# Export row-level results
df.to_csv("row_level_results.csv", index=False)

print("\nRow-level results saved to row_level_results.csv")
print(df[[
    "txn_id", "amount", "date",
    "missing_value_fail", "negative_amount_fail",
    "duplicate_txn_fail", "invalid_date_fail",
    "future_date_fail", "row_status"
]])

# --------------------------
# STEP 8: Create Clean Data Output
# --------------------------

# Keep only rows where row_status == PASS
clean_df = df[df["row_status"] == "PASS"]

# Export clean dataset
clean_df.to_csv("clean_transactions.csv", index=False)

print("\nClean data saved to clean_transactions.csv")
print(clean_df[["txn_id", "amount", "date", "country", "customer_id"]])
