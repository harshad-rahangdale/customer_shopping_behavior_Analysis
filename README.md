🛍️ Customer Shopping Behavior 

📁 Project Overview
This project analyzes customer shopping behavior using a structured pipeline: raw data → Python EDA & cleaning → MySQL storage → SQL-based business analysis.


📊 Dataset Description
Source file: customer_shopping_behavior.csv
ColumnDescriptionCustomer IDUnique identifier per customerAgeCustomer ageGenderMale / FemaleItem PurchasedProduct nameCategoryProduct category (Clothing, Footwear, etc.)Purchase Amount (USD)Transaction valueLocationUS stateSizeProduct sizeColorProduct colorSeasonPurchase seasonReview RatingRating (1–5), with some nullsSubscription StatusYes / NoShipping TypeStandard, Express, Free Shipping, etc.Discount AppliedYes / NoPromo Code UsedYes / No (dropped — duplicate of Discount Applied)Previous PurchasesCount of prior purchasesPayment MethodVenmo, Cash, Credit Card, PayPal, etc.Frequency of PurchasesWeekly, Monthly, Annually, etc.

Requirements:
pandas
mysql-connector-python
sqlalchemy
pymysql
Database config:


🗄️ SQL Analysis — Business Questions Answered
File: customer_shopping_behavior_Analysis.sql
#QuestionTechnique UsedQ1Total revenue by genderGROUP BY, SUMQ2Discount users who spent above averageSubquery, WHEREQ3Top 5 products by avg review ratingAVG, ORDER BY, LIMITQ4Avg purchase: Standard vs Express shippingFiltered GROUP BYQ5Do subscribers spend more?COUNT, AVG, SUMQ6Products with highest discount rate %CASE WHEN, percentage calcQ7Customer segmentation: New / Returning / LoyalCTE, CASE WHENQ8Top 3 products per categoryCTE, ROW_NUMBER(), window functionQ9Repeat buyers vs subscription statusFiltered GROUP BYQ10Revenue by age groupSUM, GROUP BY

⚙️ How to Run
1. Python EDA
bashpip install pandas sqlalchemy pymysql mysql-connector-python
python customer_shopping_behavior_EDA.py

Update the file path and DB credentials in the script before running.

2. SQL Analysis
sqlUSE customer_behavior;
-- Then run queries from the .sql file

Requires MySQL running locally with the Customer_behavior database created.


🔑 Key Findings (from SQL queries)

Discount buyers can still be high spenders — Q2 identifies them
Subscriber vs non-subscriber revenue difference is measurable via Q5
Loyal customers (10+ purchases) are segmented separately in Q7
Category-wise top products are ranked using window functions in Q8


