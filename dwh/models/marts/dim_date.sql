WITH order_dates AS (SELECT DISTINCT CAST (purchase_timestamp AS DATE) AS date_day FROM {{ref('stg_orders')}})

SELECT 
    date_day,
    EXTRACT(YEAR FROM date_day) AS year,
    EXTRACT(MONTH FROM date_day) AS month_number,
    TO_CHAR(date_day, 'Month') AS montth_name,
    EXTRACT(QUARTER FROM date_day) AS quarter,
    TO_CHAR(date_day, 'Day') AS day_of_week
FROM order_dates ORDER BY date_day