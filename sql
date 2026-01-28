CREATE TABLE transactions (
    transaction_id VARCHAR(10),
    customer_id VARCHAR(10),
    amount DECIMAL(10,2),
    transaction_time DATETIME,
    location VARCHAR(50),
    device VARCHAR(20),
    is_fraud INT
);


1.Find High-Value Transactions (Risky)
SELECT transaction_id, customer_id, amount
FROM transactions
WHERE amount > 15000;

2.Detect Multiple Transactions by Same Customer:
SELECT customer_id, COUNT(*) AS transaction_count
FROM transactions
GROUP BY customer_id
HAVING COUNT(*) > 2;

3.Transactions at Unusual Hours:
SELECT transaction_id, customer_id, transaction_time
FROM transactions
WHERE HOUR(transaction_time) BETWEEN 0 AND 5;

4.Location Change Detection:
SELECT t1.transaction_id, t1.customer_id, t1.location
FROM transactions t1
JOIN transactions t2
ON t1.customer_id = t2.customer_id
AND t1.location <> t2.location;

5.Device Change Detection:
SELECT customer_id, COUNT(DISTINCT device) AS device_count
FROM transactions
GROUP BY customer_id
HAVING COUNT(DISTINCT device) > 1;

6.Rule-Based Fraud Flagging:
SELECT transaction_id, customer_id, amount,
CASE 
    WHEN amount > 15000 THEN 'High Risk'
    ELSE 'Normal'
END AS risk_level
FROM transactions;

7.Fraud Percentage Analysis:
SELECT 
    SUM(is_fraud) AS fraud_transactions,
    COUNT(*) AS total_transactions,
    (SUM(is_fraud)*100.0 / COUNT(*)) AS fraud_percentage
FROM transactions;

8.Top Customers with Highest Fraud Risk:
SELECT customer_id, COUNT(*) AS fraud_count
FROM transactions
WHERE is_fraud = 1
GROUP BY customer_id
ORDER BY fraud_count DESC;
