# FreshMart Sales Analysis Dashboard

## Business Problem

FreshMart generates sales through multiple products, categories and
sales channels, but management needs a clear view of **what is driving
sales and profitability and where business performance can be
improved**.

The key business problem is:

> **How can FreshMart improve profitable growth by identifying the key
> drivers of its sales and profitability across products, categories,
> sales channels and time?**

The analysis focuses on understanding overall performance, monthly
trends, category profitability, high-performing products and channel
contribution.

### Business Objective

Identify the major drivers of FreshMart's sales and profitability and
provide data-driven recommendations that can help management improve
profitable growth.

### Business Questions

The dashboard is designed to answer the following questions:

1.  **What are FreshMart's total sales, profit and order performance?**
2.  **How do FreshMart's sales and profit change over time?**
3.  **Which categories drive sales and profit?**
4.  **Which products drive sales and profit?**
5.  **Which channels drive sales and profit?**
6.  **How can FreshMart use these insights to improve profitable
    growth?**

------------------------------------------------------------------------

## Dataset / Source Details

The project uses the provided **FreshMart sales transaction dataset** in
Excel format.

### Dataset Structure

| Sheet | Purpose |
|---|---|
| `Sales_Transactions` | Cleaned transaction-level data used for the final analysis |
| `Sales_Trans` | Original/working transaction data |
| `Sales_Trans_1` | Extended transaction data used during analysis |
| `Store` | Store information including region, city, store type, target and status |
| `Employee` | Employee information and store assignment |
| `Customer` | Customer demographic and membership information |
| `Product` | Product, category, brand, price and supplier information |
| `Pivot_KPIs` | Pivot-based KPI calculations and summaries |
| `Data_Profiling` | Data-quality issues and cleaning actions |
| `Dashboard` | Final interactive Excel dashboard |

The cleaned `Sales_Transactions` sheet contains **2,500 transaction
records and 18 analytical columns**, including transaction date,
customer, product, store, employee, quantity, pricing, discount, sales,
cost, profit, payment mode, return status, sales channel, order time and
day type.

------------------------------------------------------------------------

## Dashboard                      

The cleaned `Sales_Transactions` sheet contains **2,500 sales
transactions** and **18 analytical columns**, including transaction
date, customer, product, store, employee, quantity, pricing, discount,
sales, cost, profit, payment mode, return status, sales channel, order
time and day type.

![FreshMart Dashboard](Dashboard/Dashboard_Freshmart.png)

------------------------------------------------------------------------

## Tools / Excel Techniques Used

The project was developed using **Microsoft Excel** and the following
techniques:

-   Excel Tables
-   Data profiling
-   Power Query
-   Data type correction and standardization
-   Duplicate identification
-   Missing-value identification
-   Find & Replace
-   Conditional Formatting
-   PivotTables
-   PivotCharts
-   Slicers
-   KPI cards
-   Aggregation of Sales, Profit and Orders
-   Monthly trend analysis
-   Category and product analysis
-   Sales-channel analysis
-   Interactive dashboard design

------------------------------------------------------------------------

## Data Cleaning / Preparation

Before building the dashboard, the transaction data was profiled to
identify data-quality issues.

### Cleaning Performed

1.  **Duplicate invoice numbers**
    -   Approximately 20 duplicate invoice occurrences were identified
        during profiling for review.
2.  **Transaction date formatting**
    -   Inconsistent date formats were standardized.
    -   Date values were converted into a consistent usable date format.
3.  **Missing Customer IDs**
    -   8 blank Customer ID values were identified.
4.  **Missing Product IDs**
    -   6 blank Product ID values were identified.
5.  **Missing Store IDs**
    -   4 blank Store ID values were identified.
6.  **Missing Employee IDs**
    -   5 blank Employee ID values were identified.
7.  **Quantity validation**
    -   6 records were flagged for quantity-related checking.
8.  **Sales Amount formatting**
    -   Currency/text inconsistencies were removed so that Sales Amount
        could be treated as a numeric field.
9.  **Payment Mode standardization**
    -   Inconsistent payment-mode values were standardized using Find &
        Replace.
10. **Order Time formatting**
    -   Order Time was converted from text into a usable time/number
        format.

After cleaning and validation, the `Sales_Transactions` sheet was used
as the primary source for the dashboard analysis.

------------------------------------------------------------------------

## KPIs / Features Explained

The dashboard contains four primary KPI cards.

### Total Sales

**₹28,94,663**

Represents the total sales amount generated from the 2,500 analyzed
transactions.

### Total Profit

**₹7,37,359**

Represents the total profit generated after accounting for the recorded
cost amount.

### Total Orders

**2,500**

Represents the number of transaction/invoice records analyzed.

### Average Sales

**₹1,158**

Represents the average sales value per transaction.

### Dashboard Filters

The dashboard provides interactive slicers for:

-   Year
-   Sales Channel
-   Product Category

These filters allow management to explore the dashboard from different
business perspectives.

------------------------------------------------------------------------

## Dashboard Features

The dashboard uses business questions instead of generic chart headings
so that each visualization directly answers a management question.

### How do FreshMart's sales and profit change over time?

A line chart compares monthly Sales Amount and Profit.

**Business use:** - Identify stronger and weaker months. - Compare sales
movement with profit movement. - Support planning for promotions and
inventory.

### Which categories drive sales and profit?

A horizontal clustered bar chart compares Sales Amount and Profit across
product categories.

**Business use:** - Identify high-sales categories. - Identify
high-profit categories. - Compare revenue contribution with
profitability.

### Which products drive sales and profit?

A ranked horizontal bar chart compares Sales Amount and Profit for the
top-performing products.

**Business use:** - Identify products that contribute strongly to
revenue. - Identify products that also generate meaningful profit. -
Support inventory and promotional decisions.

### Which channels drive sales and profit?

A channel comparison chart evaluates Sales Amount and Profit across:

-   In-Store
-   Online
-   Mobile App

**Business use:** - Identify the dominant revenue channel. - Compare
profitability across channels. - Identify opportunities to strengthen
weaker channels.

------------------------------------------------------------------------

## Key Insights

Based on the cleaned transaction data and dashboard analysis:

### 1. FreshMart generated ₹28.95 lakh in sales

The dataset contains **2,500 transactions**, generating approximately
**₹28.95 lakh in sales** and **₹7.37 lakh in profit**.

### 2. In-Store is the dominant sales channel

In-Store generated approximately **₹19.91 lakh in sales**, followed by:

-   Online --- approximately **₹6.15 lakh**
-   Mobile App --- approximately **₹2.89 lakh**

This indicates that the physical-store channel is currently FreshMart's
strongest revenue contributor.

### 3. Beverages is the highest-sales category

Beverages generated approximately **₹4.75 lakh in sales**, making it the
highest-sales category.

Other major categories include:

-   Bakery --- approximately ₹3.65 lakh
-   Dairy --- approximately ₹3.54 lakh
-   Snacks --- approximately ₹2.92 lakh

### 4. Bakery generates the highest category profit

Bakery generated approximately **₹1.49 lakh in profit**, higher than
Beverages despite having lower sales.

This demonstrates that the category with the highest sales does not
necessarily generate the highest profit.

### 5. High-performing products should be monitored

The top-selling products include:

-   Harvest Gold Rusk 1kg
-   Coca-Cola Coffee 500g
-   Nescafe Coffee 1kg
-   Nestle Curd 1kg
-   Nescafe Soft Drinks Pack

These products should be monitored for stock availability and demand
continuity.

### 6. Sales and profit fluctuate across months

The monthly trend shows variation in both sales and profit. October is
the strongest month in the available data, with approximately **₹3.44
lakh in sales** and **₹85,183 in profit**.

This indicates that FreshMart should monitor monthly performance rather
than relying only on overall totals.

### 7. Sales performance should be evaluated together with profitability

A high sales value does not automatically mean the strongest business
contribution. Comparing Sales Amount and Profit by category, product and
channel helps management identify areas that support **profitable
growth** rather than revenue alone.

------------------------------------------------------------------------

## Recommendations / Conclusion

### Recommendations

Based on the analysis, FreshMart should:

-   Maintain strong inventory availability for high-sales products and
    categories.
-   Continue supporting Beverages as the leading sales category while
    protecting Bakery because of its strong profit contribution.
-   Evaluate products using both sales and profit before prioritizing
    promotions.
-   Maintain the strong In-Store channel while exploring opportunities
    to increase Online and Mobile App contribution.
-   Monitor monthly sales and profit trends to identify weaker periods
    early.
-   Use targeted promotions rather than relying only on broad discounts.
-   Compare sales and profitability together when evaluating business
    performance.
-   Use the dashboard filters to investigate performance by year,
    channel and product category.

### Conclusion

The FreshMart analysis shows that the business has strong overall sales
and profitability, but performance differs significantly across
categories, products, channels and months.

The analysis therefore recommends a **profitable-growth approach**:
maintain high-performing products and categories, protect profitable
segments, strengthen channel performance and use monthly trends to
support better planning.

The dashboard converts the cleaned transaction data into an interactive
decision-support tool that helps management understand **where sales
come from, where profit is generated and where improvement opportunities
exist**.

------------------------------------------------------------------------

## Project Outcome

This project demonstrates practical skills in:

-   Excel data cleaning
-   Power Query
-   Data profiling
-   Data analysis
-   PivotTables and PivotCharts
-   KPI development
-   Interactive dashboard creation
-   Sales and profitability analysis
-   Product and category analysis
-   Channel performance analysis
-   Business insight generation
-   Data-driven recommendations

The final output is an interactive **FreshMart Sales Analysis
Dashboard** designed to convert raw transaction data into clear and
actionable business insights.
