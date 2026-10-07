WITH source AS (
    SELECT * FROM {{ source('raw', 'orders') }}
),

renamed AS (
    SELECT
        order_id,
        customer_id,
        order_status,
        -- Cast text to proper timestamp
        CAST(order_purchase_timestamp AS TIMESTAMP) AS purchase_timestamp,
        CAST(order_approved_at AS TIMESTAMP) AS approved_at,
        CAST(order_delivered_carrier_date AS TIMESTAMP) AS carrier_date,
        CAST(order_delivered_customer_date AS TIMESTAMP) AS delivered_at,
        CAST(order_estimated_delivery_date AS TIMESTAMP) AS estimated_delivery
    FROM source
)

SELECT * FROM renamed