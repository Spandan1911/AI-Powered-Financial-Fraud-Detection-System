"""
generate_dataset.py
Generates a realistic synthetic credit-card-transaction dataset, mimicking
the structure of the popular Kaggle "Credit Card Fraud Detection" dataset
(anonymized PCA-style features V1-V14, Amount, Time, Class).

Run this once to create data/transactions.csv used by the rest of the app.
"""

import numpy as np
import pandas as pd
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(OUT_DIR, exist_ok=True)


def generate_dataset(n_samples: int = 20000, fraud_ratio: float = 0.015, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    n_fraud = int(n_samples * fraud_ratio)
    n_normal = n_samples - n_fraud

    n_features = 14  # V1..V14 (PCA-like anonymized features)

    # Normal transactions: centered around 0, tight distribution
    normal_features = rng.normal(loc=0.0, scale=1.0, size=(n_normal, n_features))

    # Fraudulent transactions: shifted mean + higher variance (anomalous pattern)
    fraud_shift = rng.normal(loc=2.5, scale=1.0, size=n_features)
    fraud_features = rng.normal(loc=fraud_shift, scale=2.5, size=(n_fraud, n_features))

    features = np.vstack([normal_features, fraud_features])
    labels = np.array([0] * n_normal + [1] * n_fraud)

    # Transaction amount: fraud tends to have unusual amounts (very small or very large)
    normal_amount = rng.gamma(shape=2.0, scale=50, size=n_normal)
    fraud_amount = np.concatenate([
        rng.uniform(0.5, 5, size=n_fraud // 2),
        rng.uniform(500, 5000, size=n_fraud - n_fraud // 2)
    ])
    rng.shuffle(fraud_amount)
    amounts = np.concatenate([normal_amount, fraud_amount])

    # Time (seconds since first transaction, over ~2 days)
    times = rng.uniform(0, 172800, size=n_samples)

    df = pd.DataFrame(features, columns=[f"V{i+1}" for i in range(n_features)])
    df["Amount"] = amounts
    df["Time"] = times
    df["Class"] = labels

    # Shuffle rows
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)

    # Add a synthetic TransactionID
    df.insert(0, "TransactionID", [f"TXN{100000+i}" for i in range(len(df))])

    return df


if __name__ == "__main__":
    df = generate_dataset()
    out_path = os.path.join(OUT_DIR, "transactions.csv")
    df.to_csv(out_path, index=False)
    print(f"Generated dataset: {out_path}")
    print(f"Shape: {df.shape}")
    print(f"Fraud ratio: {df['Class'].mean():.4f}")
