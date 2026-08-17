# FreshMart Sales Analysis Dashboard


### 1. Problem Statement

FreshMart has a large volume of sales transaction data covering
different products, categories, customers, stores, employees, dates, and
sales channels. The objective is to transform this raw transaction data
into a clean and interactive dashboard that helps management understand:

-   Overall sales and profit performance
-   Order volume and average order value
-   Monthly sales and profit trends
-   Best-performing product categories
-   Top-performing products
-   Performance across sales channels
-   Areas where sales and profitability can be improved

------------------------------------------------------------------------

## 2. Dataset / Source Details

The project uses the provided **FreshMart sales transaction dataset** in
Excel format.

### Dataset structure

  -----------------------------------------------------------------------
  Sheet                               Purpose
  ----------------------------------- -----------------------------------
  `Sales_Transactions`                Cleaned transaction-level data used
                                      for analysis

  `Sales_Trans`                       Original/working transaction data

  `Sales_Trans_1`                     Extended transaction data used
                                      during the analysis

  `Store`                             Store information such as region,
                                      city, type, target and status

  `Employee`                          Employee details and store
                                      assignment

  `Customer`                          Customer demographic and membership
                                      information

  `Product`                           Product, category, brand, price and
                                      supplier information

  `Pivot_KPIs`                        Pivot-based KPI calculations and
                                      summaries

  `Data_Profiling`                    Data-quality issues identified and
                                      cleaning actions

  `Dashboard`                         Final interactive dashboard
  -----------------------------------------------------------------------

The cleaned `Sales_Transactions` sheet contains **2,500 sales
transactions** and **18 analytical columns**, including transaction
date, customer, product, store, employee, quantity, pricing, discount,
sales, cost, profit, payment mode, return status, sales channel, order
time and day type.

------------------------------------------------------------------------

## 3. Tools / Excel Techniques Used

The project was developed using **Microsoft Excel** and the following
techniques:

-   Excel Tables
-   Power Query for data preparation
-   Data type correction and standardization
-   Duplicate identification
-   Blank/null value identification
-   Find & Replace for standardizing inconsistent values
-   Conditional Formatting for data-quality checks
-   PivotTables
-   PivotCharts
-   Slicers for interactive filtering
-   `GETPIVOTDATA` for KPI extraction
-   Aggregation of Sales, Profit and Orders
-   Dashboard layout and KPI cards
-   Trend, category, product and channel analysis

------------------------------------------------------------------------

## 4. Data Cleaning / Analysis Explanation

Several data-quality issues were identified and addressed before
creating the dashboard.

### Cleaning performed

1.  **Duplicate invoice numbers**
    -   Duplicate invoice records were identified.
    -   The data-profiling sheet records approximately 20 duplicate
        invoice occurrences for review.
2.  **Transaction date formatting**
    -   Different date formats were standardized into a consistent date
        format.
    -   Data types were corrected using Excel/Power Query techniques.
3.  **Missing Customer IDs**
    -   8 blank Customer ID values were identified.
4.  **Missing Product IDs**
    -   6 blank Product ID values were identified.
5.  **Missing Store IDs**
    -   4 blank Store ID values were identified.
6.  **Missing Employee IDs**
    -   5 blank Employee ID values were identified.
7.  **Quantity validation**
    -   6 records were flagged during the profiling process for
        quantity-related checking.
8.  **Sales amount formatting**
    -   Currency symbols/text inconsistencies were removed so that Sales
        Amount could be treated as a numeric field.
9.  **Payment mode standardization**
    -   Inconsistent payment-mode values were standardized using Find &
        Replace.
10. **Order time**

-   Order Time was originally stored as text and was converted into a
    usable time/number format.

After cleaning and validation, the cleaned transaction table was used as
the basis for the dashboard analysis.

------------------------------------------------------------------------

## 5. KPIs / Features Explained

The dashboard contains four major KPI cards:

### Total Sales

**₹28,94,662.90**

Represents the total sales amount generated from the analyzed
transactions.

### Total Profit

**₹7,37,358.89**

Represents the total profit generated after accounting for the recorded
cost amount.

### Total Orders

**2,500**

Represents the total number of transaction/invoice records analyzed.

### Average Sales

**₹1,157.87**

Represents the average sales value per transaction.

### Dashboard Filters

The dashboard also provides interactive slicers for:

-   Year
-   Sales Channel
-   Product

These filters allow users to analyze the dashboard from different
business perspectives.

------------------------------------------------------------------------

## 6. Dashboard Features

The dashboard includes the following visualizations:

### Monthly Sales & Profit Trend

A line chart compares monthly sales and profit to identify changes in
performance over time.

### Sales & Profit by Category

A category-level comparison shows how different product categories
contribute to sales and profit.

### Top 10 Products

A ranked chart highlights the products generating the highest sales
amounts.

### Sales by Channel

A comparison of **In-Store, Mobile App and Online** sales channels shows
where customers generate the most revenue.

![alt text](Dashboard_Freshmart-1.png)

------------------------------------------------------------------------

## 7. Key Insights

Based on the cleaned transaction data and dashboard analysis:

### 1. Strong overall sales performance

FreshMart generated approximately **₹28.95 lakh in sales** and **₹7.37
lakh in profit** across **2,500 transactions**.

### 2. In-Store is the dominant sales channel

In-Store sales contribute approximately **₹19.91 lakh**, making it the
largest sales channel.

Online contributes approximately **₹6.15 lakh**, while Mobile App
contributes approximately **₹2.89 lakh**.

This indicates that the physical-store experience remains the primary
revenue driver.

### 3. Beverages is the highest-sales category

**Beverages** generated approximately **₹4.75 lakh in sales**, making it
the strongest category by sales value.

Other strong categories include:

-   Bakery --- approximately ₹3.65 lakh
-   Dairy --- approximately ₹3.54 lakh
-   Snacks --- approximately ₹2.92 lakh

### 4. Bakery is a major profit contributor

Although Beverages has the highest sales, **Bakery generates the highest
profit** among the categories, at approximately **₹1.49 lakh**.

This indicates that sales volume alone does not determine profitability.

### 5. Product concentration

The top-selling products include products such as:

-   Harvest Gold Rusk 1kg
-   Coca-Cola Coffee 500g
-   Nescafe Coffee 1kg
-   Nestle Curd 1kg
-   Nescafe Soft Drinks Pack

These products should be closely monitored for stock availability and
repeat demand.

### 6. Monthly performance varies considerably

The monthly trend shows noticeable fluctuations in sales and profit. In
the available 2026 records, **March** is the strongest month by sales,
with approximately **₹1.53 lakh**, while sales decline considerably in
several later months.

This suggests that seasonal demand, promotions, product availability or
customer behavior may influence monthly performance.

------------------------------------------------------------------------

## 8. Recommendations / Conclusion

### Recommendations

1.  **Strengthen high-performing categories**
    -   Maintain sufficient inventory for Beverages, Bakery, Dairy and
        Snacks.
    -   Use targeted promotions for categories that have strong profit
        potential.
2.  **Improve digital-channel performance**
    -   In-Store is currently the dominant channel, while Mobile App and
        Online contribute less.
    -   FreshMart can increase digital sales through app-exclusive
        offers, loyalty rewards and personalized promotions.
3.  **Focus on profitable products**
    -   Track both sales and profit when deciding which products to
        promote.
    -   High-sales products should not be evaluated only by revenue;
        their profit contribution should also be considered.
4.  **Use monthly trends for planning**
    -   Prepare inventory and promotional campaigns based on periods of
        higher demand.
    -   Investigate months with unusually low sales to identify possible
        operational or demand-related issues.
5.  **Improve data quality continuously**
    -   Customer, Product, Store and Employee IDs should be validated at
        the time of data entry.
    -   Duplicate invoice numbers and missing identifiers should be
        monitored regularly.

### Conclusion

The FreshMart dashboard converts raw retail transaction data into a
simple, interactive business-reporting solution. The analysis shows that
FreshMart has a strong in-store revenue base, with Beverages leading
sales and Bakery showing particularly strong profitability.

The dashboard can help management make better decisions related to
inventory planning, product promotions, channel strategy and sales
performance monitoring.

------------------------------------------------------------------------


## 9. Project Outcome

This project demonstrates practical skills in:

-   Excel data cleaning
-   Power Query
-   Data analysis
-   PivotTables and PivotCharts
-   KPI creation
-   Dashboard development
-   Business insight generation
-   Data-driven recommendations

The final output is an interactive FreshMart sales dashboard designed to
support quick and effective business decision-making.
