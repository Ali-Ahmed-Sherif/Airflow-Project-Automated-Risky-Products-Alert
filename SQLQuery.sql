
use Sales_DataMart_2022;

CREATE VIEW Products_summary AS
SELECT
    p.product_name,
    p.product_category,
    SUM(f.extended_sales) AS total_sales,
    SUM(f.freight) AS total_freight,
    SUM(f.extened_cost) AS total_cogs,
    SUM(f.tax_amount) AS total_tax_collected,
    

    (SUM(f.extended_sales) + SUM(f.freight)) AS net_revenue,

    (
        (SUM(f.extended_sales) + SUM(f.freight))
        - SUM(f.extened_cost)
        - SUM(f.tax_amount)
    ) AS net_profit,
    

    CONCAT(
        ROUND(
            (
                (SUM(f.extended_sales) + SUM(f.freight))
                - SUM(f.extened_cost)
                - SUM(f.tax_amount)
            )
            / (SUM(f.extended_sales) + SUM(f.freight)) * 100,
        2),
        '%'
    ) AS net_margin,
    

    CASE 
        WHEN ((SUM(f.extended_sales) + SUM(f.freight)) - SUM(f.extened_cost) - SUM(f.tax_amount)) < 0 
        THEN 'Risky (Negative Profit)' 
        ELSE 'Potential (Positive Profit)'
    END AS product_status_flag  
    
FROM dim_product AS p
JOIN fact_sales AS f
    ON p.product_key = f.product_key
GROUP BY p.product_name, p.product_category;


select * from Products_summary;