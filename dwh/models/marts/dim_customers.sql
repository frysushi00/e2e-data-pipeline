WITH raw_customers AS (
    SELECT * FROM {{source('raw', 'customers')}}
),
deduplicated AS (
    SELECT customer_id, customer_city, customer_state,
        customer_zip_code_prefix,
        ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY customer_id) as rn
    FROM raw_customers
)
SELECT customer_id, customer_city, customer_state, customer_zip_code_prefix FROM deduplicated
WHERE rn = 1