import pandas as pd
import numpy as np

# 📥 Cargar dataset
df = pd.read_csv("data/raw/creditcard.csv")

# 🧹 Seleccionar columnas
df = df[["Time", "Amount", "Class"]]

# 🔄 Renombrar
df = df.rename(columns={
    "Time": "transaction_date",
    "Amount": "amount",
    "Class": "is_fraud"
})

# 🔥 ARREGLAR TIPOS (CLAVE)
df["transaction_date"] = df["transaction_date"].astype(int)
df["is_fraud"] = df["is_fraud"].astype(int)

# 👤 customer_id
df["customer_id"] = np.random.randint(1, 501, size=len(df)).astype(int)

# 🌍 country
countries = ["Spain", "France", "Germany", "Italy"]
df["country"] = np.random.choice(countries, size=len(df))

# 📊 Orden
df = df[["transaction_date", "customer_id", "amount", "country", "is_fraud"]]

# 💾 Guardar limpio
df.to_csv("data/processed/fraud_clean.csv", index=False)

print("✅ Dataset transformado correctamente")