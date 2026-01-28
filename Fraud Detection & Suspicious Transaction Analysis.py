import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Transaction_ID': ['T001','T002','T003','T004','T005'],
    'Customer_ID': ['C101','C101','C101','C205','C205'],
    'Amount': [500, 450, 25000, 800, 18000],
    'Time': ['10:15','10:18','10:19','14:10','14:11'],
    'Location': ['Chennai','Chennai','Russia','Delhi','Delhi'],
    'Device': ['Mobile','Mobile','Web','POS','Web'],
    'Is_Fraud': [0,0,1,0,1]
}

df = pd.DataFrame(data)
df

df.info()
df.describe()

df['High_Value_Flag'] = df['Amount'].apply(lambda x: 1 if x > 15000 else 0)
df[['Transaction_ID','Amount','High_Value_Flag']]

df['Transaction_Count'] = df.groupby('Customer_ID')['Transaction_ID'].transform('count')
df[['Customer_ID','Transaction_ID','Transaction_Count']]

df['Location_Change'] = df.groupby('Customer_ID')['Location'].transform(
    lambda x: x != x.iloc[0]
).astype(int)

df[['Transaction_ID','Customer_ID','Location','Location_Change']]

df['Device_Change'] = df.groupby('Customer_ID')['Device'].transform(
    lambda x: x != x.iloc[0]
).astype(int)

df[['Transaction_ID','Customer_ID','Device','Device_Change']]

df['Fraud_Score'] = (
    df['High_Value_Flag'] +
    df['Location_Change'] +
    df['Device_Change']
)

df[['Transaction_ID','Fraud_Score']]

df['Fraud_Flag'] = df['Fraud_Score'].apply(lambda x: 'Fraud' if x >= 2 else 'Normal')
df[['Transaction_ID','Fraud_Flag']]


plt.figure()
plt.scatter(df['Transaction_ID'], df['Amount'])
plt.title("Transaction Amount Distribution")
plt.xlabel("Transaction ID")
plt.ylabel("Amount")
plt.show()
