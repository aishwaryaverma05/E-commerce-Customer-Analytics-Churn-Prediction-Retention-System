CREATE DATABASE ecommerce_project;
USE ecommerce_project;
SELECT * FROM transactions LIMIT 5;
SELECT COUNT(*) FROM transactions;
SELECT COUNT(DISTINCT Invoice) AS Total_Orders FROM transactions;
ALTER TABLE transactions RENAME COLUMN ï»¿Invoice TO Invoice;
SELECT COUNT(DISTINCT Customer_ID) AS Total_Customers FROM transactions WHERE Customer_ID IS NOT NULL;
ALTER TABLE transactions RENAME COLUMN `Customer ID` TO `Customer_ID`;
SELECT SUM(Quantity*Price) AS Total_Revenue FROM transactions WHERE Quantity>0;
SELECT SUM(Quantity) AS Total_Quantity FROM transactions WHERE Quantity > 0;
SELECT YEAR(str_to_date(InvoiceDate, '%d-%m-%Y %H:%i')) AS year, MONTH(str_to_date(InvoiceDate, '%d-%m-%Y %H:%i')) AS month, SUM(Quantity*Price) AS Monthly_Revenue FROM transactions WHERE Quantity>0 GROUP BY YEAR(str_to_date(InvoiceDate, '%d-%m-%Y %H:%i')), MONTH(str_to_date(InvoiceDate, '%d-%m-%Y %H:%i')) ORDER BY year, month;
SELECT InvoiceDate FROM transactions LIMIT 10;
SELECT str_to_date(InvoiceDate, '%d-%m-%Y %H:%i') AS Converted_date from transactions limit 5;
SELECT Country,sum(Quantity*Price) AS Country_Revenue from transactions where Quantity>0 GROUP BY(Country) order by (Country_Revenue) DESC;
SELECT Description ,sum(Quantity*Price) AS Product_Revenue from transactions where Quantity>0 GROUP BY Description order by Product_Revenue DESC;
SELECT Customer_ID ,sum(Quantity*Price) AS Customer_Revenue from transactions where (Quantity>0 and Customer_ID is not null) GROUP BY Customer_ID order by Customer_Revenue DESC limit 10;
select Customer_ID,count(distinct Invoice) as Customer_frequency from transactions where customer_ID is not null group by Customer_ID order by Customer_frequency desc;
SELECT MAX(STR_TO_DATE(InvoiceDate, '%d-%m-%Y %H:%i')) AS Latest_Date FROM transactions;
SELECT Customer_ID, DATEDIFF('2011-01-18', DATE(MAX(STR_TO_DATE(InvoiceDate, '%d-%m-%Y %H:%i')))) AS Recency FROM transactions WHERE Customer_ID IS NOT NULL GROUP BY Customer_ID ORDER BY Recency asc;
SELECT Customer_ID,
    DATEDIFF(
        '2011-01-18',
        DATE(MAX(STR_TO_DATE(InvoiceDate, '%d-%m-%Y %H:%i')))
    ) AS Recency,
    COUNT(DISTINCT Invoice) AS Frequency,
    SUM(Quantity * Price) AS Monetary
FROM transactions WHERE Customer_ID IS NOT NULL
AND Quantity > 0 GROUP BY Customer_ID ORDER BY Monetary DESC;
SELECT Customer_ID, DATE_FORMAT(MIN(STR_TO_DATE(InvoiceDate, '%d-%m-%Y %H:%i')), '%Y-%m') AS Cohort_Month
FROM transactions WHERE Customer_ID IS NOT NULL AND Quantity > 0 GROUP BY Customer_ID;
SELECT DATE_FORMAT(STR_TO_DATE(InvoiceDate, '%d-%m-%Y %H:%i'), '%Y-%m') AS Purchase_Month, COUNT(DISTINCT Customer_ID) AS Active_Customers FROM transactions
WHERE Customer_ID IS NOT NULL AND Quantity > 0 GROUP BY Purchase_Month ORDER BY Purchase_Month;
SELECT c.Cohort_Month, DATE_FORMAT(STR_TO_DATE(t.InvoiceDate, '%d-%m-%Y %H:%i'), '%Y-%m') AS Purchase_Month,COUNT(DISTINCT t.Customer_ID) AS Customers
FROM transactions t JOIN (SELECT Customer_ID, DATE_FORMAT(MIN(STR_TO_DATE(InvoiceDate, '%d-%m-%Y %H:%i')), '%Y-%m') AS Cohort_Month
FROM transactions WHERE Customer_ID IS NOT NULL AND Quantity > 0 GROUP BY Customer_ID) c
ON t.Customer_ID = c.Customer_ID WHERE t.Customer_ID IS NOT NULL AND t.Quantity > 0 GROUP BY c.Cohort_Month, Purchase_Month ORDER BY c.Cohort_Month, Purchase_Month;
SELECT c.Cohort_Month, DATE_FORMAT(STR_TO_DATE(t.InvoiceDate, '%d-%m-%Y %H:%i'), '%Y-%m') AS Purchase_Month, COUNT(DISTINCT t.Customer_ID) AS Customers
FROM transactions t JOIN (SELECT Customer_ID, DATE_FORMAT( MIN(STR_TO_DATE(InvoiceDate, '%d-%m-%Y %H:%i')), '%Y-%m' ) AS Cohort_Month FROM transactions WHERE Customer_ID IS NOT NULL AND Quantity > 0 GROUP BY Customer_ID) c ON t.Customer_ID = c.Customer_ID WHERE t.Customer_ID IS NOT NULL AND t.Quantity > 0 GROUP BY c.Cohort_Month, Purchase_Month ORDER BY c.Cohort_Month, Purchase_Month;
WITH cohort_data AS (SELECT c.Cohort_Month, DATE_FORMAT(STR_TO_DATE(t.InvoiceDate, '%d-%m-%Y %H:%i'),'%Y-%m') AS Purchase_Month,
COUNT(DISTINCT t.Customer_ID) AS Customers FROM transactions t JOIN (
SELECT Customer_ID,DATE_FORMAT(MIN(STR_TO_DATE(InvoiceDate, '%d-%m-%Y %H:%i')), '%Y-%m'
) AS Cohort_Month FROM transactions WHERE Customer_ID IS NOT NULL AND Quantity > 0
GROUP BY Customer_ID) c ON t.Customer_ID = c.Customer_ID WHERE t.Customer_ID IS NOT NULL AND t.Quantity > 0
GROUP BY c.Cohort_Month, Purchase_Month)
SELECT Cohort_Month,
    Purchase_Month,
    Customers,
    ROUND(
        Customers * 100.0 /
        FIRST_VALUE(Customers) OVER (
            PARTITION BY Cohort_Month
            ORDER BY Purchase_Month
        ),
        2
    ) AS Retention_Percent
FROM cohort_data
ORDER BY Cohort_Month, Purchase_Month;


