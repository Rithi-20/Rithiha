# TrendKart Fashion Sales Analysis Dashboard

## 1. Project Overview

**TrendKart Fashion Sales Analysis** is an Excel-based business
intelligence project developed to analyze fashion retail transaction
data and convert it into meaningful business insights through an
interactive dashboard.

The project focuses on sales, profit, product/category performance,
sales-channel performance, regional performance, and monthly sales
trends. The final dashboard uses PivotTables, PivotCharts, slicers, and
data-cleaning techniques to provide a simple and interactive view of
business performance.

### Problem Statement

TrendKart operates across multiple regions, stores, products, customers,
employees, and sales channels. With a large volume of transaction data,
it can be difficult to quickly understand which categories, products,
channels, and regions are contributing most to revenue and profit.

The objective of this project is to clean and analyze the raw retail
dataset and create an interactive dashboard that helps management:

-   Monitor total sales and profit
-   Identify high-performing product categories
-   Identify top-performing products
-   Compare offline and online sales
-   Compare regional performance
-   Analyze monthly sales and profit trends
-   Identify data-quality issues that may affect reporting
-   Make data-driven business decisions

------------------------------------------------------------------------

## 2. Dataset / Source Details

The project uses the provided **TrendMart Fashion Enterprise Dataset**
in Excel format.

### Dataset overview

  ------------------------------------------------------------------------
  Data Area                                  Records Purpose
  --------------------- ---------------------------- ---------------------
  Sales Transactions                           3,000 Transaction-level
                                                     sales data used for
                                                     analysis

  Customers                                      850 Customer
                                                     demographics, region
                                                     and membership
                                                     details

  Products                                       250 Product, category,
                                                     brand, pricing and
                                                     supplier details

  Stores                                         120 Store, location,
                                                     region and target
                                                     information

  Employees                                      300 Employee, department,
                                                     designation and
                                                     performance
                                                     information

  Suppliers                                       90 Supplier details,
                                                     lead time and
                                                     supplier ratings
  ------------------------------------------------------------------------

### Main workbook sheets

  -----------------------------------------------------------------------
  Sheet                               Purpose
  ----------------------------------- -----------------------------------
  `Sales_Transactions`                Cleaned transaction-level dataset

  `Sales`                             Combined sales analysis dataset
                                      with related customer, product,
                                      store and employee attributes

  `Customers` / `Customer`            Customer master data

  `Products` / `Product`              Product master data

  `Stores` / `Store`                  Store master data

  `Employees` / `Employee`            Employee master data

  `Suppliers` / `Supplier`            Supplier master data

  `Pivot_Analysis`                    Pivot-based calculations used for
                                      dashboard analysis

  `Dashboard`                         Dashboard worksheet

  `Data_Profiling`                    Data-quality issues identified
                                      during profiling
  -----------------------------------------------------------------------

### Transaction period

The sales transaction data covers **April 2024 to March 2025**.

------------------------------------------------------------------------

## 3. Tools / Excel Techniques Used

The project was developed using **Microsoft Excel** with the following
techniques:

-   Excel Tables
-   Data profiling
-   Data cleaning and standardization
-   Duplicate identification
-   Missing-value identification
-   Date-format standardization
-   Text and numeric data-type correction
-   Find & Replace
-   Conditional Formatting
-   PivotTables
-   PivotCharts
-   Slicers
-   KPI cards
-   Aggregation of Sales Amount and Profit
-   Category, product, channel and regional analysis
-   Monthly trend analysis
-   Interactive dashboard design

------------------------------------------------------------------------

## 4. Data Cleaning / Analysis Explanation

Before building the dashboard, the dataset was profiled to identify
data-quality problems.

### Sales transaction issues identified

The profiling sheet identified issues including:

-   **5 duplicate invoice numbers**
-   **6 blank Customer IDs**
-   **5 blank Product IDs**
-   **5 blank Employee IDs**
-   **6 mixed date-format records**
-   **5 Quantity values stored as text**
-   **4 Payment Mode records containing extra spaces**
-   **4 negative-profit records**
-   **5 records with Quantity = 0**
-   **5 mixed Payment Mode casing issues**
-   **4 Return Status spelling/format issues**

### Master-data issues identified

Additional issues were found in the supporting tables:

**Customers** - 5 duplicate phone numbers - 5 invalid email records - 5
inconsistent gender values - 5 inconsistent membership values - 5 names
with leading/trailing spaces

**Products** - 4 duplicate product names - 4 incorrect category
spellings - 4 blank brand values

**Stores** - 3 missing manager names - 2 status typos

**Employees** - 2 employee names with leading/trailing spaces - 2
employment-status typos

These issues were reviewed and standardized so that the final analysis
could be performed consistently.

------------------------------------------------------------------------

## 5. KPIs / Features Explained

The dashboard highlights two primary business KPIs:

### Total Sales

**₹92,27,179.96**

This represents the total sales value generated from the 3,000 analyzed
transactions.

### Total Profit

**₹18,01,437.12**

This represents the total profit generated from the analyzed
transactions.

### Additional analytical metrics

From the transaction dataset:

-   **Total transactions:** 3,000
-   **Average sales per transaction:** approximately ₹3,075.73
-   **Overall profit margin:** approximately 19.52%

### Dashboard Filters

The dashboard provides interactive slicers for:

-   Store Region
-   Product
-   Sales Channel

These filters allow users to dynamically explore the dashboard based on
different business segments.

------------------------------------------------------------------------

## 6. Dashboard Features

The TrendKart dashboard contains four major analytical sections.

### 1. Monthly Performance & Profit Trend

A line chart compares Sales Amount and Profit across the transaction
period.

This helps identify:

-   High-performing months
-   Low-performing periods
-   Changes in revenue and profitability
-   Potential seasonal patterns

### 2. Sales & Profit by Category

A category-level chart compares sales and profit across fashion
categories.

Major categories include:

-   Women Sarees
-   Handbags
-   Watches
-   Jewellery
-   Women Dresses
-   Footwear
-   Men Ethnic
-   Women Jeans
-   Women Kurtis
-   Winter Wear
-   Sportswear
-   Accessories
-   And other fashion categories

### 3. Top 10 Products

The dashboard ranks the highest-performing products based on sales
amount.

This helps management identify products that contribute significantly to
revenue and may require stronger inventory planning and promotional
attention.

### 4. Sales by Channel

The dashboard compares:

-   Offline
-   Online

Offline sales are the dominant channel, while Online sales provide an
important secondary revenue stream.

### 5. Sales by Region

The dashboard compares performance across:

-   South Zone 1
-   South Zone 2
-   South Zone 3

This allows management to identify which regions are generating the
highest revenue and profit.

------------------------------------------------------------------------

## 7. Key Insights

### 1. Strong overall revenue generation

TrendKart generated approximately **₹92.27 lakh in sales** and **₹18.01
lakh in profit** from 3,000 transactions.

The overall profit margin is approximately **19.52%**, indicating a
healthy contribution from the analyzed sales.

### 2. Offline is the dominant sales channel

Offline sales generated approximately **₹60.49 lakh**, while Online
sales generated approximately **₹31.78 lakh**.

Offline therefore contributes around **65.6% of total sales**, making
physical retail the primary revenue channel.

However, Online contributes approximately **34.4%**, showing that
digital sales already represent a significant part of the business.

### 3. Women Sarees is the highest-sales category

**Women Sarees** generated approximately **₹11.03 lakh**, making it the
highest-sales category in the transaction data.

Other major categories include:

-   Handbags --- approximately ₹9.94 lakh
-   Watches --- approximately ₹9.38 lakh
-   Jewellery --- approximately ₹8.51 lakh
-   Women Dresses --- approximately ₹6.48 lakh

These categories represent important revenue drivers for TrendKart.

### 4. Handbags has the highest profit among the major categories

Handbags generated approximately **₹2.14 lakh in profit**, which is
higher than the profit generated by Women Sarees.

This shows that the category generating the highest sales does not
necessarily generate the highest profit.

Management should therefore evaluate both **sales value and
profitability** when deciding which categories to prioritize.

### 5. South Zone 1 is the strongest region

South Zone 1 generated approximately **₹44.63 lakh in sales** and
**₹8.65 lakh in profit**.

South Zone 2 generated approximately **₹25.55 lakh in sales**, while
South Zone 3 generated approximately **₹22.09 lakh**.

South Zone 1 therefore contributes nearly half of the total sales and is
the strongest regional market.

### 6. October 2024 was the strongest sales month

October 2024 generated approximately **₹15.19 lakh in sales** and
**₹3.01 lakh in profit**, making it the strongest month in the
transaction period.

This suggests that seasonal demand, promotional activity or customer
purchasing patterns may have contributed to the increase.

### 7. Product concentration should be monitored

The transaction data shows a small group of products contributing
substantially to overall sales.

For example, **GRT Jewellers Sling Bag Olive** generated approximately
**₹4.83 lakh in sales** and **₹1.15 lakh in profit**, making it a
particularly strong product in the analyzed data.

High-performing products should be monitored carefully for stock
availability and demand continuity.

------------------------------------------------------------------------

## 8. Recommendations / Conclusion

### Recommendations

1.  **Maintain inventory for high-performing categories**
    -   Prioritize Women Sarees, Handbags, Watches and Jewellery.
    -   Avoid stock-outs for products with consistently high sales.
2.  **Strengthen the online channel**
    -   Offline sales are currently dominant, but Online contributes
        more than one-third of total sales.
    -   Introduce online-exclusive offers, personalized recommendations
        and loyalty incentives to increase digital purchases.
3.  **Use region-specific strategies**
    -   South Zone 1 is the strongest region and should be used as a
        benchmark for other regions.
    -   Investigate why South Zone 2 and South Zone 3 have lower sales
        and identify opportunities to improve local performance.
4.  **Focus on profitability, not only sales**
    -   Handbags demonstrate that a category can generate higher profit
        even when it is not the highest-sales category.
    -   Product and category decisions should consider both revenue and
        profit margin.
5.  **Plan promotions around high-demand periods**
    -   October 2024 showed particularly strong performance.
    -   Historical monthly trends can be used to plan inventory and
        marketing campaigns ahead of expected demand peaks.
6.  **Improve data quality at the source**
    -   Duplicate invoices, missing IDs, inconsistent payment modes and
        incorrect status values should be prevented through validation
        rules.
    -   Regular data-quality checks will improve the reliability of
        future dashboards.

### Conclusion

The TrendKart Fashion Sales Dashboard transforms 3,000 retail
transactions into an interactive business intelligence solution.

The analysis shows that TrendKart has a strong offline sales base, Women
Sarees is the leading sales category, South Zone 1 is the strongest
region, and October 2024 was the highest-sales month in the analyzed
period.

The dashboard can support management in making better decisions related
to inventory planning, regional strategy, online-channel growth, product
promotion and profitability improvement.

------------------------------------------------------------------------

## 9. Dashboard Preview

The final TrendKart dashboard provides an interactive view of sales and
profit performance using KPI cards, slicers and multiple charts.

`<img src="./Dashboard_Trendkart.png" alt="TrendKart Sales Dashboard" width="100%">`{=html}

------------------------------------------------------------------------

## 10. Project Outcome

This project demonstrates practical skills in:

-   Excel data cleaning
-   Data profiling
-   Data analysis
-   PivotTables and PivotCharts
-   KPI development
-   Interactive dashboard creation
-   Business insight generation
-   Sales and profitability analysis
-   Regional and channel analysis
-   Data-driven recommendations

The final output is an interactive **TrendKart Fashion Sales Dashboard**
designed to convert raw retail data into clear and actionable business
insights.
