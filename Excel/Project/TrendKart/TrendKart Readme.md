# TrendKart Fashion Sales Analysis Dashboard

## Business Problem

### Why did TrendKart sales fall sharply in November 2024 compared with October 2024?

TrendKart recorded its strongest monthly sales in **October 2024 at ₹15.19 lakh**, but sales fell to **₹10.54 lakh in November 2024**, a **30.6% month-on-month decline**.

The decline was mainly driven by **fewer orders**, not by customers spending less per order. Orders decreased from **512 to 351 (31.4%)**, while quantity sold fell from **1,046 to 712 (31.9%)**. In contrast, average order value actually increased slightly from **₹2,967 to ₹3,004 (1.2%)**.

This means the key business problem is a **drop in transaction/customer volume after the October sales peak**.

### What contributed to the decline?

- **Offline sales** fell by approximately **₹3.47 lakh (34.1%)**, making it the largest channel-level contributor to the decline.
- **Online sales** also fell by approximately **₹1.18 lakh (23.5%)**.
- **Handbags** fell by **46.9%**, **Women Sarees by 43.7%**, and **Footwear by 42.9%**.
- **South Zone 1**, the largest region, fell by approximately **₹2.45 lakh (32.7%)**.
- **South Zone 2** declined by **38.0%**.
- **Weekend sales** fell by **42.7%**, compared with a **25.3%** decline on weekdays.
- Credit Card sales fell by **50.0%**, while EMI sales fell by **47.7%**.
- Profit decreased from **₹3.01 lakh to ₹1.95 lakh**, a **35.4% decline**.

The decline is therefore broad-based, but the largest pressure came from the **offline channel, high-value fashion categories, South Zone 1, and weekend transactions**.

### Solution

TrendKart should focus on **recovering customer/order traffic after the October peak**, while retaining the higher average order value.

1. **Rebuild post-October customer traffic**
   - Launch November retention campaigns for customers who purchased during October.
   - Use loyalty points, personalized offers and limited-time promotions to encourage repeat purchases.
   - Measure success using order count and repeat-customer rate, not only revenue.

2. **Strengthen the offline channel**
   - Since Offline sales fell by ₹3.47 lakh, investigate store-level performance in the affected regions.
   - Use in-store promotions and category-specific displays for high-performing products.

3. **Recover high-impact categories**
   - Prioritize Handbags, Women Sarees, Watches, Footwear and Men Ethnic because their sales declined substantially.
   - Check inventory levels and identify whether stock availability contributed to the decline.

4. **Target weekend demand**
   - Weekend sales dropped 42.7%, so TrendKart can introduce weekend-only offers, events and bundled fashion deals.
   - Use store-level promotions in locations with the largest weekend decline.

5. **Protect the strongest region**
   - South Zone 1 lost approximately ₹2.45 lakh in sales.
   - Compare store performance within South Zone 1 to identify underperforming stores and replicate successful October practices where appropriate.

6. **Use October as a benchmark, not as the normal baseline**
   - October was an unusually strong month, so management should compare November with both October and the longer-term monthly average.
   - This avoids treating a seasonal peak as the normal sales level.

**Business objective:** Recover lost transaction volume and improve post-peak customer retention while maintaining the average order value and profitability.

---

## Dataset / Source Details

The project uses the provided **TrendKart Fashion Enterprise Dataset** in Excel format.

### Dataset structure

| Sheet / Data | Details |
|---|---|
| `Sales Transactions` | 3,000 transaction-level sales records used for analysis |
| `Customers` | 850 customer demographics, region and membership details |
| `Products` | 250 product, category, brand, pricing and supplier details |
| `Stores` | 120 store, location, region and target information |
| `Employees` | 300 employee, department, designation and performance information |
| `Suppliers` | 90 supplier details, lead time and supplier ratings |

The sales transaction data covers **April 2024 to March 2025**.

![TrendKart Dashboard](Dashboard/Dashboard_Trendkart.png)

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
- Category, product, channel and regional analysis
- Monthly trend analysis
- Interactive dashboard design

---

## Data Cleaning / Analysis Explanation

Before building the dashboard, the dataset was profiled to identify data-quality problems.

### Cleaning performed

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

### Master-data cleaning

Additional issues were identified in the supporting tables:

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

After cleaning and validation, the transaction and supporting tables were used as the basis for the dashboard analysis.

---

## KPIs / Features Explained

The dashboard highlights the following major KPIs:

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

Represents the overall profit generated as a percentage of total sales.

### Dashboard Filters

The dashboard provides interactive slicers for:

- Store Region
- Product
- Sales Channel

These filters allow users to dynamically explore the dashboard based on different business segments.

---

## Dashboard Features

The TrendKart dashboard includes the following visualizations:

### Monthly Sales & Profit Trend

A line chart compares monthly Sales Amount and Profit across the transaction period.

This helps identify changes in sales and profitability over time.

### Sales & Profit by Category

A category-level comparison shows how different fashion categories contribute to sales and profit.

Major categories include:

- Women Sarees
- Handbags
- Watches
- Jewellery
- Women Dresses
- Footwear
- Men Ethnic
- Women Jeans
- Women Kurtis
- Winter Wear
- Sportswear
- Accessories
- Other fashion categories

### Top 10 Products

A ranked chart highlights the products generating the highest sales amounts.

This helps management identify products that contribute significantly to revenue and may require stronger inventory planning and promotional attention.

### Sales by Channel

A comparison of **Offline and Online** sales channels shows where customers generate the most revenue.

Offline sales are the dominant channel, while Online sales provide an important secondary revenue stream.

### Sales by Region

The dashboard compares performance across:

- South Zone 1
- South Zone 2
- South Zone 3

This allows management to identify which regions are generating the highest revenue and profit.

---

## Key Insights

Based on the cleaned transaction data and dashboard analysis:

### 1. Strong overall revenue generation

TrendKart generated approximately **₹92.27 lakh in sales** and **₹18.01 lakh in profit** from **3,000 transactions**.

The overall profit margin is approximately **19.52%**, indicating a healthy contribution from the analyzed sales.

### 2. Offline is the dominant sales channel

Offline sales generated approximately **₹60.49 lakh**, while Online sales generated approximately **₹31.78 lakh**.

Offline therefore contributes around **65.6% of total sales**, making physical retail the primary revenue channel.

However, Online contributes approximately **34.4%**, showing that digital sales already represent a significant part of the business.

### 3. Women Sarees is the highest-sales category

**Women Sarees** generated approximately **₹11.03 lakh**, making it the highest-sales category in the transaction data.

Other major categories include:

- Handbags — approximately ₹9.94 lakh
- Watches — approximately ₹9.38 lakh
- Jewellery — approximately ₹8.51 lakh
- Women Dresses — approximately ₹6.48 lakh

These categories represent important revenue drivers for TrendKart.

### 4. Handbags has the highest profit among the major categories

Handbags generated approximately **₹2.14 lakh in profit**, which is higher than the profit generated by Women Sarees.

This shows that the category generating the highest sales does not necessarily generate the highest profit.

Management should therefore evaluate both **sales value and profitability** when deciding which categories to prioritize.

### 5. South Zone 1 is the strongest region

South Zone 1 generated approximately **₹44.63 lakh in sales** and **₹8.65 lakh in profit**.

South Zone 2 generated approximately **₹25.55 lakh in sales**, while South Zone 3 generated approximately **₹22.09 lakh**.

South Zone 1 therefore contributes nearly half of the total sales and is the strongest regional market.

### 6. October 2024 was the strongest sales month

October 2024 generated approximately **₹15.19 lakh in sales** and **₹3.01 lakh in profit**, making it the strongest month in the transaction period.

This suggests that seasonal demand, promotional activity or customer purchasing patterns may have contributed to the increase.

### 7. Product concentration should be monitored

The transaction data shows a small group of products contributing substantially to overall sales.

For example, **GRT Jewellers Sling Bag Olive** generated approximately **₹4.83 lakh in sales** and **₹1.15 lakh in profit**, making it a particularly strong product in the analyzed data.

High-performing products should be monitored carefully for stock availability and demand continuity.

---

## Recommendations / Conclusion

### Recommendations

Based on the data-backed business problem above, TrendKart should:

- Focus on **order/customer volume**, because the 31.4% fall in orders was the main reason for the November sales decline.
- Use **post-purchase campaigns** to convert October customers into repeat buyers.
- Strengthen the **Offline channel**, which accounted for the largest absolute sales decline.
- Prioritize **Handbags, Women Sarees, Watches and Footwear** for stock checks and targeted promotions.
- Investigate store-level performance in **South Zone 1 and South Zone 2**.
- Introduce **weekend-specific campaigns** because weekend sales dropped 42.7%.
- Monitor payment-channel changes, particularly the large decline in **Credit Card and EMI** transactions.
- Compare each month against both the previous month and the **historical average**, because October was an unusually strong sales peak.

### Conclusion

The TrendKart analysis shows that the November 2024 sales decline was primarily a **volume problem**. Sales fell 30.6% because the number of orders dropped 31.4%, while average order value remained broadly stable.

The recommended response is therefore to recover customer traffic and repeat purchases, strengthen the offline channel, target the categories and regions with the largest declines, and use weekend promotions to rebuild transaction volume.

This converts the dashboard from a reporting tool into a decision-making tool by directly connecting the observed sales decline to measurable business actions.

---

## Project Outcome

This project demonstrates practical skills in:

- Excel data cleaning
- Data profiling
- Data analysis
- PivotTables and PivotCharts
- KPI development
- Interactive dashboard creation
- Business insight generation
- Sales and profitability analysis
- Regional and channel analysis
- Data-driven recommendations

The final output is an interactive **TrendKart Fashion Sales Dashboard** designed to convert raw retail data into clear and actionable business insights.
