import pandas as pd
import random
from datetime import datetime, timedelta

data = []

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 2, 10)

for i in range(1, 101):
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)

    data.append([
        f"T{i:03}",
        f"U{random.randint(1, 30):02}",
        f"M{random.randint(1, 10):02}",
        random_date.strftime("%Y-%m-%d"),
        f"{random.randint(0, 23):02}:{random.randint(0, 59):02}",
        random.randint(100, 80000),
        random.choice(["UPI", "Card", "Wallet", "NetBanking"]),
        random.choice(["Chennai", "Bangalore", "Delhi", "Mumbai", "Hyderabad", "Pune"]),
        random.choice(["Mobile", "Laptop"]),
        random.choice(["Success", "Failed"]),
        random.choice([0, 0, 0, 0, 1])
    ])

df = pd.DataFrame(data, columns=[
    "Transaction_ID", "User_ID", "Merchant_ID", "Date", "Time", "Amount",
    "Payment_Method", "Location", "Device_Type", "Status", "Is_Fraud"
])

df.to_csv("fraud_dataset.csv", index=False)
print("CSV file created!")
