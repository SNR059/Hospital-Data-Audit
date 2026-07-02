import pandas as pd
import numpy as np

# 1. Load and Clean Currency
df = pd.read_csv("metropolis_patient_data.csv")
df["Total_Charge"] = df["Total_Charge"].str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)

# 2. Deduplicate the WHOLE table
df = df.drop_duplicates(subset="Record_ID")

# 3. Handle Dates & Duration
df["Admit_Date"] = pd.to_datetime(df["Admit_Date"])
df["Discharge_Date"] = pd.to_datetime(df["Discharge_Date"]) # NaT stays NaT (Not a Time)

# Calculate days (only for those who have a discharge date)
df["Stay_Duration"] = (df["Discharge_Date"] - df["Admit_Date"]).dt.days

# 4. Outlier Logic (IQR)
Q1 = df["Stay_Duration"].quantile(0.25)
Q3 = df["Stay_Duration"].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + (1.5 * IQR)

# Flagging Expensive Cases (90th percentile)
threshold_90 = df["Total_Charge"].quantile(0.90)
df["Is_Expensive"] = df["Total_Charge"] > threshold_90
Python
# 1. Clean Currency (Removing $ and , then making it a number)
df["Total_Charge"] = df["Total_Charge"].str.replace("$", "", regex=False)
df["Total_Charge"] = df["Total_Charge"].str.replace(",", "", regex=False).astype(float)

# 2. Deduplicate (Cleaning the WHOLE table based on ID)
df = df.drop_duplicates(subset="Record_ID")

# 3. Stay Duration (Getting the integer number of days)
df["Admit_Date"] = pd.to_datetime(df["Admit_Date"])
df["Discharge_Date"] = pd.to_datetime(df["Discharge_Date"])
df["Stay_Duration"] = (df["Discharge_Date"] - df["Admit_Date"]).dt.days
# The 'Left' join keeps every patient, even if their department is missing overhead data
final_df = pd.merge(df, specialty_costs, on="Department", how="left")

# Calculating the Hospital's Bottom Line
final_df["Operating_Cost"] = final_df["Stay_Duration"] * final_df["Daily_Overhead"]
final_df["Profit"] = final_df["Total_Charge"] - final_df["Operating_Cost"]
# Group by the Department, then find the average of the Profit column
dept_performance = final_df.groupby("Department")["Profit"].mean()
print(dept_performance)
import seaborn as sns
import matplotlib.pyplot as plt

# The 'Col' creates the side-by-side comparison
sns.relplot(data=final_df, x="Stay_Duration", y="Total_Charge", col="Department", hue="Is_Expensive", kind="scatter")
plt.show()
Action Recommendation: Keep the budget for Pediatric department as before. Double check for any premium insurances responsible for the outliers. Review of all involved insurances is suggested.
