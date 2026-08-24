# TrendKart Fashion Sales Analysis Dashboard

## Business Problem

### Why did TrendKart's sales fall sharply in November 2024 compared with October 2024?

TrendKart recorded its strongest monthly sales in **October 2024 at approximately ₹15.19 lakh**, but sales fell to **approximately ₹10.54 lakh in November 2024**, representing a **30.6% month-on-month decline**.

The decline was mainly driven by a reduction in transaction volume. Orders decreased from **512 to 351 (31.4%)**, while quantity sold decreased from **1,046 to 712 (31.9%)**. In contrast, average order value increased slightly from approximately **₹2,967 to ₹3,004 (1.2%)**.

This indicates that the November decline was primarily a **volume problem rather than a reduction in customer spending per order**.

### What contributed to the decline?

- **Offline sales** fell by approximately **₹3.47 lakh (34.1%)**, making it the largest channel-level contributor.
- **Online sales** fell by approximately **₹1.18 lakh (23.5%)**.
- **Handbags** declined by approximately **46.9%**.
- **Women Sarees** declined by approximately **43.7%**.
- **Footwear** declined by approximately **42.9%**.
- **South Zone 1** declined by approximately **32.7%** and recorded the largest absolute regional decline.
- **South Zone 2** declined by approximately **38.0%**.
- **Weekend sales** fell by approximately **42.7%**, compared with a **25.3%** decline on weekdays.
- Profit decreased from approximately **₹3.01 lakh to ₹1.95 lakh**, a **35.4% decline**.

The decline is therefore broad-based, with significant pressure coming from transaction volume, the Offline channel, major fashion categories and key regions.

### Business Objective

**Recover lost transaction volume and improve post-peak customer retention while maintaining average order value and profitability.**

### Solution

TrendKart should focus on recovering customer and order traffic after the October peak while using the dashboard to identify the products, categories, channels and regions that experienced the largest decline.

1. **Recover transaction volume**
   - Focus on increasing order/customer traffic rather than only increasing average order value.
   - Use October customers as a target group for repeat-purchase campaigns.
   - Track order count and average order value together.

2. **Strengthen the affected sales channels**
   - Investigate the Offline channel because it recorded the largest absolute sales decline.
   - Review Online performance and identify opportunities to recover lost digital sales.

3. **Recover high-impact categories and products**
   - Prioritize categories with the largest October-to-November decline.
   - Identify products with the highest sales loss and investigate inventory, demand and promotional performance.

4. **Investigate regional performance**
   - Review South Zone 1 and South Zone 2 at store level.
   - Identify stores that experienced the largest decline and compare their October and November performance.

5. **Use the dashboard for ongoing monitoring**
   - Compare monthly sales and profit.
   - Monitor channel, category, product and regional changes.
   - Use October as a strong benchmark while also considering longer-term monthly performance.

---

## Dataset / Source Details

The project uses the provided **TrendKart Fashion Enterprise Dataset** in Excel format.

### Dataset Structure

| Sheet / Data | Details |
|---|---|
| `Sales Transactions` | 3,000 transaction-level sales records used for analysis |
| `Customers` | 850 customer demographic, region and membership details |
| `Products` | 250 product, category, brand, pricing and supplier details |
| `Stores` | 120 store, location, region and target information |
| `Employees` | 300 employee, department, designation and performance information |
| `Suppliers` | 90 supplier details, lead time and supplier ratings |

The sales transaction data covers **April 2024 to March 2025**.

---

## Dashboard

The TrendKart dashboard converts the business problem into focused analytical questions. Each visualization is designed to identify where the October-to-November sales decline occurred.

![TrendKart Dashboard](Dashboard/Dashboard_Trendkart.png)

### How the dashboard addresses the business problem

| Business Question | Dashboard Solution | Business Use |
|---|---|---|
| **How did sales and profit change over time?** | Monthly Sales & Profit line chart | Identifies the October peak and November decline |
| **Which categories drove the sales decline?** | October vs November category comparison | Identifies categories with significant sales reductions |
| **Which products lost the most sales?** | Top 10 products ranked by sales decline | Identifies products requiring investigation |
| **Which channels lost sales?** | October vs November channel comparison | Identifies the channel contributing most to the decline |
| **Which regions lost sales?** | October vs November regional comparison | Identifies regions requiring further investigation |

---

## Tools / Excel Techniques Used

The project was developed using **Microsoft Excel** and the following techniques:

- Excel Tables
- Data profiling
- Data cleaning and standardization
- Duplicate identification
- Missing-value identification
- Date-format standardization
- Text and numeric data-type correction
- Find & Replace
- Conditional Formatting
- PivotTables
- PivotCharts
- Slicers
- KPI cards
- Aggregation of Sales Amount and Profit
- Monthly trend analysis
- October vs November comparison
- Category analysis
- Product decline analysis
- Sales-channel analysis
- Regional analysis
- Interactive dashboard design

---

## Data Cleaning / Analysis Explanation

Before building the dashboard, the dataset was profiled to identify data-quality problems.

### Cleaning Performed

1. **Duplicate invoice numbers**
   - 5 duplicate invoice numbers were identified.

2. **Missing Customer IDs**
   - 6 blank Customer IDs were identified.

3. **Missing Product IDs**
   - 5 blank Product IDs were identified.

4. **Missing Employee IDs**
   - 5 blank Employee IDs were identified.

5. **Mixed date formats**
   - 6 mixed date-format records were identified and standardized.

6. **Quantity stored as text**
   - 5 Quantity values were stored as text and required correction.

7. **Payment Mode spacing**
   - 4 Payment Mode records contained extra spaces.

8. **Negative-profit records**
   - 4 negative-profit records were identified for review.

9. **Zero quantity records**
   - 5 records had Quantity = 0.

10. **Payment Mode casing**
    - 5 mixed Payment Mode casing issues were identified.

11. **Return Status formatting**
    - 4 Return Status spelling/format issues were identified.

### Master-data Cleaning

**Customers**
- 5 duplicate phone numbers
- 5 invalid email records
- 5 inconsistent gender values
- 5 inconsistent membership values
- 5 names with leading/trailing spaces

**Products**
- 4 duplicate product names
- 4 incorrect category spellings
- 4 blank brand values

**Stores**
- 3 missing manager names
- 2 status typos

**Employees**
- 2 employee names with leading/trailing spaces
- 2 employment-status typos

These issues were reviewed and standardized so that the final analysis could be performed consistently.

---

## KPIs / Features Explained

### Total Sales

**₹92,27,179.96**

Represents the total sales value generated from the **3,000 analyzed transactions**.

### Total Profit

**₹18,01,437.12**

Represents the total profit generated from the analyzed transactions.

### Total Transactions

**3,000**

Represents the total number of transaction records analyzed.

### Average Sales per Transaction

**Approximately ₹3,075.73**

Represents the average sales value per transaction.

### Overall Profit Margin

**Approximately 19.52%**

Represents total profit as a percentage of total sales.

### Dashboard Filters

The dashboard provides interactive slicers for:

- Store Region
- Product
- Sales Channel

These filters allow users to explore the dashboard based on different business segments.

---

## Dashboard Features

### How did sales and profit change over time?

A **line chart** compares monthly Sales Amount and Profit across the transaction period.

The chart highlights the strong October 2024 performance and the sharp November 2024 decline.

### Which categories drove the sales decline?

An **October vs November clustered column chart** compares Sales Amount by product category.

This identifies categories with significant sales reductions and helps prioritize inventory and promotional review.

### Which products lost the most sales?

A **horizontal bar chart** ranks the top 10 products by their October-to-November Sales Decline.

**Sales Decline = October Sales − November Sales**

Only products with an actual sales decline are considered.

This identifies products with the largest sales losses and supports targeted recovery actions.

### Which channels lost sales?

A **clustered column chart** compares October and November Sales Amount for the Offline and Online channels.

This identifies the channel contributing most to the decline and supports channel-specific recovery strategies.

### Which regions lost sales?

A **clustered column chart** compares October and November Sales Amount across TrendKart's regions.

This helps identify regions with significant sales reductions and areas requiring further store-level investigation.

---

## Key Insights

Based on the cleaned transaction data and dashboard analysis:

### 1. November sales declined significantly after the October peak

October 2024 generated approximately **₹15.19 lakh in sales**, while November generated approximately **₹10.54 lakh**, representing a **30.6% decline**.

### 2. The decline was primarily a transaction-volume problem

Orders fell from **512 to 351**, a **31.4% decrease**.

Quantity sold also declined from **1,046 to 712**, a **31.9% decrease**.

However, average order value increased slightly from approximately **₹2,967 to ₹3,004**.

This indicates that TrendKart's main issue was **fewer transactions rather than lower spending per order**.

### 3. Offline was the largest channel contributor to the decline

Offline sales fell by approximately **₹3.47 lakh (34.1%)**, while Online sales fell by approximately **₹1.18 lakh (23.5%)**.

This makes Offline the most important channel to investigate for recovery.

### 4. Several major categories experienced substantial declines

Handbags declined by approximately **46.9%**, Women Sarees by **43.7%**, and Footwear by **42.9%** from October to November.

These categories should be prioritized for further investigation.

### 5. Regional performance also weakened

South Zone 1 declined by approximately **32.7%** and recorded the largest absolute regional sales decline.

South Zone 2 declined by approximately **38.0%**.

This suggests that store-level investigation in these regions could help identify the source of lost sales.

### 6. Profit declined faster than sales

Profit decreased from approximately **₹3.01 lakh in October to ₹1.95 lakh in November**, a **35.4% decline**.

This reinforces the need to recover sales volume while protecting profitability.

### 7. Overall business performance remains substantial

Across the full analyzed dataset, TrendKart generated approximately **₹92.27 lakh in sales** and **₹18.01 lakh in profit** from **3,000 transactions**, with an overall profit margin of approximately **19.52%**.

---

## Recommendations / Conclusion

### Recommendations

Based on the business problem and dashboard analysis, TrendKart should:

- Focus on **recovering order/customer volume**, since the fall in orders was the main driver of the November decline.
- Use **post-purchase campaigns** to encourage October customers to return.
- Strengthen the **Offline channel**, which recorded the largest absolute sales decline.
- Prioritize **Handbags, Women Sarees and Footwear** for inventory checks and targeted promotions.
- Investigate **South Zone 1 and South Zone 2** at store level.
- Identify products with the **largest October-to-November sales decline** and review their availability and demand.
- Use targeted campaigns to recover weaker periods without unnecessarily reducing average order value.
- Compare monthly performance against both the previous month and the longer-term trend so that a strong seasonal peak is not treated as the normal baseline.

### Conclusion

The TrendKart analysis shows that the November 2024 sales decline was primarily a **volume problem**. Sales fell by 30.6% because order volume declined by 31.4%, while average order value remained broadly stable.

The dashboard therefore focuses on identifying **where the lost sales came from** across categories, products, channels and regions and converts those findings into targeted business actions.

The recommended approach is to **recover transaction volume, strengthen the affected sales channels, target products and categories with significant declines, and investigate underperforming regions while maintaining profitability**.

---

## Project Outcome

This project demonstrates practical skills in:

- Excel data cleaning
- Data profiling
- Data analysis
- PivotTables and PivotCharts
- KPI development
- Interactive dashboard creation
- Monthly trend analysis
- Sales decline analysis
- Product and category analysis
- Regional and channel analysis
- Business insight generation
- Data-driven recommendations

The final output is an interactive **TrendKart Fashion Sales Dashboard** designed to convert raw retail transaction data into clear, actionable business insights and support data-driven decision-making.
