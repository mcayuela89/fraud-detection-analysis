import pandas as pd
import numpy as np


df = pd.read_csv("data/raw/creditcard.csv")


df = df[["Time", "Amount", "Class"]]


df = df.rename(columns={
    "Time": "transaction_date",
    "Amount": "amount",
    "Class": "is_fraud"
})


df["transaction_date"] = df["transaction_date"].astype(int)
df["is_fraud"] = df["is_fraud"].astype(int)


df["customer_id"] = np.random.randint(1, 501, size=len(df)).astype(int)


countries = ["Spain", "France", "Germany", "Italy"]
df["country"] = np.random.choice(countries, size=len(df))


df = df[["transaction_date", "customer_id", "amount", "country", "is_fraud"]]


df.to_csv("data/processed/fraud_clean.csv", index=False)

print("✅ Dataset transformado correctamente")