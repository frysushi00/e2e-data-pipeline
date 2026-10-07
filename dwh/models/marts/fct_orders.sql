WITH orders AS (
    SELECT * FROM {{ source('raw', 'orders') }}
),
order_items AS (
    SELECT order_id, product_id FROM {{ source('raw', 'order_items') }}
)

SELECT 
    o.order_id,
    o.customer_id,
    i.product_id,
    CAST(o.order_purchase_timestamp AS DATE) AS order_date,
    o.order_status,
    EXTRACT(DAY FROM (CAST(o.order_delivered_customer_date AS TIMESTAMP) - CAST(o.order_purchase_timestamp AS TIMESTAMP))) AS delivery_delay_days
FROM orders o
LEFT JOIN order_items i ON o.order_id = i.order_id