# PROJECT 2: EXPLORATORY DATA ANALYSIS
# DecodeLabs Internship - Project 2

import pandas as pd
import numpy as np

print("=" * 50)
print("EXPLORATORY DATA ANALYSIS - STARTING...")
print("=" * 50)

# Load the cleaned data from Project 1
df = pd.read_excel('../Dataset_Cleaned.xlsx')

print(f"\nLoaded: {len(df)} rows")

# -------------------------------------------------------------------
# PART 1: BASIC STATISTICS
# -------------------------------------------------------------------

print("\n--- Total Price Stats ---")
total_prices = df['TotalPrice']

print(f"Count: {len(total_prices)}")
print(f"Average: ${total_prices.mean():.2f}")
print(f"Median: ${total_prices.median():.2f}")
print(f"Minimum: ${total_prices.min():.2f}")
print(f"Maximum: ${total_prices.max():.2f}")

print("\n--- Quantity Stats ---")
quantities = df['Quantity']

print(f"Average quantity: {quantities.mean():.1f}")
print(f"Most common quantity: {quantities.mode()[0]}")
print(f"Minimum: {quantities.min()}")
print(f"Maximum: {quantities.max()}")

print("\n--- Unit Price Stats ---")
unit_prices = df['UnitPrice']

print(f"Average price: ${unit_prices.mean():.2f}")
print(f"Median price: ${unit_prices.median():.2f}")
print(f"Minimum: ${unit_prices.min():.2f}")
print(f"Maximum: ${unit_prices.max():.2f}")

# -------------------------------------------------------------------
# PART 2: CATEGORICAL ANALYSIS
# -------------------------------------------------------------------

print("\n--- Product Popularity ---")
product_counts = df['Product'].value_counts()
print(product_counts)

print("\n--- Payment Methods ---")
payment_counts = df['PaymentMethod'].value_counts()
print(payment_counts)

print("\n--- Order Status ---")
status_counts = df['OrderStatus'].value_counts()
print(status_counts)

print("\n--- Referral Sources ---")
referral_counts = df['ReferralSource'].value_counts()
print(referral_counts)

# -------------------------------------------------------------------
# PART 3: FINDING OUTLIERS
# -------------------------------------------------------------------

print("\n--- Looking for Unusual Orders ---")

Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['TotalPrice'] < lower_bound) | (df['TotalPrice'] > upper_bound)]

print(f"Normal range: ${lower_bound:.2f} to ${upper_bound:.2f}")
print(f"Outliers found: {len(outliers)}")

if len(outliers) > 0:
    print("\nOutlier orders:")
    print(outliers[['OrderID', 'TotalPrice', 'Product']].head(10))

# -------------------------------------------------------------------
# PART 4: SUMMARY
# -------------------------------------------------------------------

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)

print(f"Total orders: {len(df)}")
print(f"Total revenue: ${df['TotalPrice'].sum():.2f}")
print(f"Average order value: ${df['TotalPrice'].mean():.2f}")
print(f"Most popular product: {df['Product'].mode()[0]}")
print(f"Most common payment method: {df['PaymentMethod'].mode()[0]}")
print(f"Most common order status: {df['OrderStatus'].mode()[0]}")
print(f"Most common referral source: {df['ReferralSource'].mode()[0]}")
print(f"Outliers found: {len(outliers)}")

# Additional check - high-value orders
print("\n--- High Value Orders ---")
high_value = df[df['TotalPrice'] > 3000]
print(f"Orders over $3000: {len(high_value)}")
if len(high_value) > 0:
    print(high_value[['OrderID', 'TotalPrice', 'Product']].head(5))