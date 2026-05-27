select * from superstore;

#1.Total sales and Total profit
SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore;

#2.Top 10 Prodects by Sales
SELECT
    `Product Name`,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10;

#Sales by resion
SELECT
    Region,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;

#Profit by category
SELECT
    Category,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC;

#monthly sales trends
SELECT
    MONTH(`Order Date`) AS Month,
    SUM(Sales) AS Monthly_Sales
FROM superstore
GROUP BY Month
ORDER BY Month;

#Top 10 costomers by sales
SELECT
    `Customer Name`,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;

#avarage shipings dates
SELECT
    AVG(DATEDIFF(`Ship Date`, `Order Date`))
    AS Avg_Shipping_Days
FROM superstore;

#Sigments wise Sales
SELECT
    Segment,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Segment;

#State wise profit
SELECT
    State,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY State
ORDER BY Total_Profit DESC;

#most profitable sub-categars
SELECT
    `Sub-Category`,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY `Sub-Category`
ORDER BY Total_Profit DESC;