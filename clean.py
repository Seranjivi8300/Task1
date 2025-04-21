import pandas as pd

# Load dataset (tab-separated)
df = pd.read_csv("marketing_campaign.csv", sep='\t')

# 1. Check missing values
print("Missing values before cleanup:\n", df.isnull().sum())

# 2. Handle missing values
df['Income'].fillna(df['Income'].mean(), inplace=True)

# 3. Remove duplicates
df = df.drop_duplicates()

# 4. Standardize text values
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.strip().str.upper()
if 'Country' in df.columns:
    df['Country'] = df['Country'].str.title()
df['Education'] = df['Education'].str.strip().str.title()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.title()

# 5. Convert date formats
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')

# 6. Rename column headers
df.columns = df.columns.str.lower().str.replace(' ', '_')

# 7. Fix data types and create new fields
df['income'] = df['income'].astype(float)
df['age'] = 2025 - df['year_birth']

# Optional: Save the cleaned data
df.to_csv("marketing_campaign_cleaned.csv", index=False)

# Print cleaned data sample
print("\n✅ Data cleaned successfully. Preview:")
print(df.head())
